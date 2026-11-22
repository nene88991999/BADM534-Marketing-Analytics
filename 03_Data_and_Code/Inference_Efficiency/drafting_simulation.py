"""Original synthetic decoding-cost comparison; no model or external service."""
import csv
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COMPATIBILITY = {"aligned": 0.85, "mismatched": 0.55, "realigned": 0.80}
PREFILL_MS = 40.0


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]),
                                lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def decode(target, uniforms, k, compatibility):
    """Count synthetic greedy-prefix progress through a fixed target ending in EOS.

    Draft proposals are capped by the known remaining output budget. The first
    incompatible proposal ends the accepted prefix. A target token then corrects
    it, or supplies a bonus after a fully accepted draft, unless EOS was accepted.
    All proposed positions incur cost, including the discarded suffix. Returned
    tokens are the fixed target by construction; this is no language-model fit.
    """
    if (not target or target[-1] != "<EOS>" or "<EOS>" in target[:-1]
            or len(uniforms) != len(target) or k < 0 or int(k) != k
            or not 0 <= compatibility <= 1
            or any(not 0 <= u < 1 for u in uniforms)):
        raise ValueError("Invalid target, uniforms, draft length, or compatibility")
    position, output, rounds = 0, [], []
    while position < len(target):
        proposed = min(k, len(target) - position)
        accepted = 0
        while (accepted < proposed
               and uniforms[position + accepted] < compatibility):
            accepted += 1
        extra = int(position + accepted < len(target))
        emitted = accepted + extra
        draft_ms = 0.25 * proposed
        verify_ms = 4.0 + 0.08 * proposed + 0.16 * proposed ** 2
        rounds.append(dict(start_position=position, proposed=proposed,
            accepted=accepted, target_token=extra, emitted=emitted,
            draft_ms=draft_ms, verify_ms=verify_ms,
            ended_with_eos=position + emitted == len(target)))
        output.extend(target[position:position + emitted])
        position += emitted
    return output, rounds


def run():
    roster, summaries, details = [], [], []
    for split, offset in (("development", 0), ("evaluation", 1000)):
        requests = []
        for i in range(12):
            length = (24, 48, 96)[i % 3]
            seed = 20261122 + offset + i
            rng = random.Random(seed)
            uniforms = [rng.random() for _ in range(length + 1)]
            target = [f"token_{j}" for j in range(length)] + ["<EOS>"]
            case = f"{split}_{i:02d}"
            roster.append(dict(request_id=case, split=split,
                content_tokens=length, eos_tokens=1, seed=seed))
            requests.append((case, target, uniforms))
        policies = [("ordinary", 0, 0.0)] + [
            (name, k, p) for name, p in COMPATIBILITY.items()
            for k in range(1, 13)]
        for name, k, probability in policies:
            emitted = accepted = proposed = passes = 0
            generation_ms = 0.0
            for case, target, uniforms in requests:
                output, rounds = decode(target, uniforms, k, probability)
                assert output == target
                for number, row in enumerate(rounds):
                    details.append(dict(request_id=case, split=split,
                        regime=name, k=k, round=number, **row))
                    emitted += row["emitted"]
                    accepted += row["accepted"]
                    proposed += row["proposed"]
                    generation_ms += row["draft_ms"] + row["verify_ms"]
                passes += len(rounds)
            total_ms = generation_ms + len(requests) * PREFILL_MS
            summaries.append(dict(split=split, regime=name, k=k,
                compatibility=probability, requests=len(requests),
                emitted_including_eos=emitted, passes=passes,
                proposed=proposed, accepted=accepted,
                block_efficiency=emitted / passes,
                generation_ms=generation_ms, total_ms=total_ms,
                generation_tokens_per_second=1000 * emitted / generation_ms,
                total_tokens_per_second=1000 * emitted / total_ms,
                mean_request_ms=total_ms / len(requests)))
    selected = []
    for name in COMPATIBILITY:
        candidates = [r for r in summaries
                      if r["split"] == "development" and r["regime"] == name]
        best = max(candidates, key=lambda r: (r["total_tokens_per_second"], -r["k"]))
        final = next(r for r in summaries if r["split"] == "evaluation"
                     and r["regime"] == name and r["k"] == best["k"])
        selected.append(dict(regime=name, selected_k=best["k"],
            development_tokens_per_second=best["total_tokens_per_second"],
            evaluation_tokens_per_second=final["total_tokens_per_second"],
            evaluation_mean_request_ms=final["mean_request_ms"]))
    write_csv(ROOT / "data/request_roster.csv", roster)
    write_csv(ROOT / "results/rounds.csv", details)
    write_csv(ROOT / "results/decoding_summary.csv", summaries)
    write_csv(ROOT / "results/frozen_choices.csv", selected)
    print(json.dumps(selected, indent=2))


if __name__ == "__main__":
    run()
