#!/usr/bin/env python3
import os, json, random
from pathlib import Path

SEED = 1337

def set_deterministic():
    random.seed(SEED)

def list_tasks(eval_dir):
    files = sorted([f for f in os.listdir(eval_dir) if f.endswith(".json")])
    print(f"Found {len(files)} tasks")
    assert len(files) == 3, f"Expected 3 tasks, found {len(files)}"
    print("Tasks sample:", files[:3])
    return files
def solve_task(task_obj):
    # TODO: replace with real logic
    return task_obj["train"][0]["output"]

def evaluate_all():
    set_deterministic()
    eval_dir = Path("evaluation")
    out_dir = Path("outputs")
    out_dir.mkdir(exist_ok=True)
    tasks = list_tasks(eval_dir)

    predictions = {}
    correct = 0
    for name in tasks:
        task = json.load(open(eval_dir / name))
        pred = solve_task(task)
        predictions[name[:-5]] = [pred]

    json.dump(predictions, open(out_dir / "predictions.json","w"), indent=2)
    summary = {"seed": SEED, "total": len(tasks), "correct": correct, "accuracy": 0.0}
    json.dump(summary, open(out_dir / "summary.json","w"), indent=2)
    print("Done: outputs/predictions.json & summary.json")

if __name__ == "__main__":
    evaluate_all()
