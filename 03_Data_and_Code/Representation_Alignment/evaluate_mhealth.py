"""Compare local word/character representations on unseen mHealth descriptions."""
import csv
import hashlib
import json
import platform
import re
from collections import Counter
from pathlib import Path
import numpy as np
from alignment import apply_map, fit_map, neighbor_overlap

HERE = Path(__file__).resolve().parent
DIMENSIONS = (8, 16, 32)
VOCABULARY = 512
PENALTY = 1.0


def tokens(text, kind):
    if kind == "word":
        return re.findall(r"\b\w+\b", text)
    marked = " " + text + " "
    return [marked[i:i+3] for i in range(len(marked)-2)]


def encode(texts, kind, state=None):
    bags = [Counter(tokens(t, kind)) for t in texts]
    if state is None:
        frequency = Counter()
        for bag in bags:
            frequency.update(bag.keys())
        vocabulary = sorted(frequency, key=lambda t: (-frequency[t], t))[:VOCABULARY]
        lookup = {t: i for i, t in enumerate(vocabulary)}
        idf = np.array([np.log((1+len(texts))/(1+frequency[t])) + 1 for t in vocabulary])
        state = lookup, idf
    lookup, idf = state
    matrix = np.zeros((len(texts), len(lookup)))
    for i, bag in enumerate(bags):
        for token, count in bag.items():
            if token in lookup:
                matrix[i, lookup[token]] = (1+np.log(count))*idf[lookup[token]]
    norm = np.linalg.norm(matrix, axis=1, keepdims=True)
    return matrix / np.where(norm > 0, norm, 1), state


def reduce_fit(matrix, dimensions):
    # Uncentered truncated SVD from the feature Gram matrix; fit on training only.
    eigenvalues, vectors = np.linalg.eigh(matrix.T @ matrix)
    return vectors[:, np.argsort(eigenvalues)[::-1][:dimensions]]


def train_classifier(values, labels, classes):
    x = np.column_stack([np.ones(len(values)), values])
    y = np.array([[float(label == c) for c in classes] for label in labels])
    penalty = np.eye(x.shape[1])*PENALTY; penalty[0, 0] = 0
    return np.linalg.solve(x.T @ x + penalty, x.T @ y)


def predict(values, coefficients, classes):
    scores = np.column_stack([np.ones(len(values)), values]) @ coefficients
    return np.asarray(classes)[scores.argmax(axis=1)]


def metrics(truth, prediction, classes):
    truth, prediction = np.asarray(truth), np.asarray(prediction)
    by_class = []
    for label in sorted(set(classes) | set(truth)):
        support = int((truth == label).sum())
        tp = int(((truth == label) & (prediction == label)).sum())
        fp = int(((truth != label) & (prediction == label)).sum())
        fn = support - tp
        by_class.append(dict(category=label, support=support, correct=tp,
                             predicted=int((prediction == label).sum()),
                             recall=tp/support if support else None,
                             f1=2*tp/(2*tp+fp+fn) if 2*tp+fp+fn else 0.0))
    return dict(cases=len(truth), correct=int((truth == prediction).sum()),
                accuracy=float((truth == prediction).mean()),
                macro_f1=float(np.mean([r["f1"] for r in by_class])), by_category=by_class)


def main():
    path = HERE / "data/descriptions.csv"
    manifest = json.loads((HERE / "manifest.json").read_text())
    if hashlib.sha256(path.read_bytes()).hexdigest() != manifest["data_sha256"]:
        raise ValueError("Description sample differs from its manifest.")
    with path.open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    splits = {s: [r for r in rows if r["split"] == s] for s in ["train", "validation", "test"]}
    ids = [{r["description"] for r in splits[s]} for s in splits]
    if any(ids[i] & ids[j] for i in range(3) for j in range(i)):
        raise ValueError("Descriptions overlap across splits.")
    classes = sorted({r["category"] for r in splits["train"]})
    labels = {s: [r["category"] for r in group] for s, group in splits.items()}
    text = {s: [r["description"] for r in group] for s, group in splits.items()}
    representations = {}
    for kind in ["word", "character"]:
        training, state = encode(text["train"], kind)
        basis = reduce_fit(training, max(DIMENSIONS))
        representations[kind] = {"train": training @ basis}
        for split in ["validation", "test"]:
            encoded, _ = encode(text[split], kind, state)
            representations[kind][split] = encoded @ basis
    test_predictions = {}

    def evaluate(dimension, split):
        word = {s: x[:, :dimension] for s, x in representations["word"].items()}
        char = {s: x[:, :dimension] for s, x in representations["character"].items()}
        fitted = fit_map(char["train"], word["train"])
        word_model = train_classifier(word["train"], labels["train"], classes)
        char_model = train_classifier(char["train"], labels["train"], classes)
        candidates = {"word_reference": word[split], "character_unmapped": char[split],
                      "character_aligned": apply_map(char[split], fitted),
                      "character_retrained": char[split]}
        scores = {}
        for name, values in candidates.items():
            model = char_model if name == "character_retrained" else word_model
            prediction = predict(values, model, classes)
            if split == "test":
                test_predictions[name] = prediction.tolist()
            score = metrics(labels[split], prediction, classes)
            score["neighbor_overlap_k10"] = neighbor_overlap(word[split], values, 10)
            score["out_of_training_categories"] = sum(y not in classes for y in labels[split])
            unambiguous = np.array([int(r["category_count"]) == 1 for r in splits[split]])
            score["unambiguous_cases"] = int(unambiguous.sum())
            score["unambiguous_accuracy"] = float((prediction[unambiguous] ==
                np.asarray(labels[split])[unambiguous]).mean()) if unambiguous.any() else None
            scores[name] = score
        return scores

    outcomes, validation = {}, []
    for dimension in DIMENSIONS:
        scores = evaluate(dimension, "validation")
        outcomes[str(dimension)] = {"validation": scores}
        validation.append(dict(dimension=dimension, accuracy=scores["character_aligned"]["accuracy"]))
    # Freeze the dimension using validation before scoring any test outcomes.
    selected = min(validation, key=lambda r: (-r["accuracy"], r["dimension"]))["dimension"]
    outcomes[str(selected)]["test"] = evaluate(selected, "test")
    result = dict(unit="Equally weighted normalized descriptions", classes=classes,
                  dimensions=list(DIMENSIONS), selected_dimension=selected, validation=validation,
                  primary_test=outcomes[str(selected)]["test"],
                  all_configurations=outcomes, source_data_sha256=manifest["data_sha256"],
                  environment={"python": platform.python_version(), "numpy": np.__version__},
                  penalty=PENALTY, vocabulary_limit=VOCABULARY, model_api_calls=0,
                  selection="Maximize aligned validation accuracy; use lower dimension on a tie")
    (HERE / "results/mhealth.json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    with (HERE / "results/test_predictions.csv").open("w", newline="") as stream:
        fields = ["description_sha256", "reference_category"] + list(test_predictions)
        writer = csv.DictWriter(stream, fieldnames=fields); writer.writeheader()
        for i, row in enumerate(splits["test"]):
            writer.writerow(dict(description_sha256=row["description_sha256"],
                                 reference_category=row["category"],
                                 **{name: values[i] for name, values in test_predictions.items()}))
    with (HERE / "results/summary.csv").open("w", newline="") as stream:
        fields = ["dimension", "split", "configuration", "cases", "correct", "accuracy",
                  "macro_f1", "neighbor_overlap_k10", "unambiguous_cases", "unambiguous_accuracy"]
        writer = csv.DictWriter(stream, fieldnames=fields); writer.writeheader()
        for dimension, splits_out in outcomes.items():
            for split, choices in splits_out.items():
                for name, score in choices.items():
                    writer.writerow(dict(dimension=dimension, split=split, configuration=name,
                                         **{k: score[k] for k in fields[3:]}))
    print(json.dumps(dict(selected_dimension=selected, validation=validation,
                         primary_test={k: {a: b for a, b in v.items() if a != "by_category"}
                                       for k, v in result["primary_test"].items()}), indent=2))


if __name__ == "__main__":
    main()
