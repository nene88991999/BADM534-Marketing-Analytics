"""A constructed generator-by-judge comparison on a fixed 0-100 rubric."""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent

def compare(scores):
    old, new = scores["old_judge"], scores["new_judge"]
    return dict(scores=scores,
        diagonal_change=new["new_generator"]-old["old_generator"],
        generator_change_old_judge=old["new_generator"]-old["old_generator"],
        generator_change_new_judge=new["new_generator"]-new["old_generator"],
        judge_change_old_generator=new["old_generator"]-old["old_generator"])

def main():
    # Scores are imposed. Both judges assess the same saved outputs for each generator.
    scores = {"old_judge": {"old_generator": 60, "new_generator": 62},
              "new_judge": {"old_generator": 75, "new_generator": 77}}
    result = compare(scores)
    assert result["diagonal_change"] == (
        result["generator_change_new_judge"]+result["judge_change_old_generator"])
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    (output / "judge_comparison.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
if __name__ == "__main__":
    main()
