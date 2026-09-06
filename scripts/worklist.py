#!/usr/bin/env python3
"""List every field where the search was not exhausted — the contributor worklist.

An `unverified` field means one of two very different things:

  search_exhausted: true   The absence is a FINDING. Somebody looked properly and
                           no admissible source exists, or the field is null by
                           design (a discredited construct, a medical record that
                           is never public, a deliberate editorial exclusion).

  search_exhausted: false  The absence is a TODO. Nobody has searched properly.

Before this flag existed the two were indistinguishable, and the dataset silently
presented "I stopped looking" as "this does not exist". That is a quieter form of
the same dishonesty the project was built to prevent: it does not fabricate a
value, it fabricates a conclusion about the record.

Usage:
    python3 scripts/worklist.py           # the todo list
    python3 scripts/worklist.py --all     # todos and findings side by side
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIRS = [ROOT / "dataset", ROOT / "cases"]


def claims(node, path=""):
    if isinstance(node, dict):
        if {"value", "confidence", "sources"} <= node.keys():
            yield path, node
            return
        for k, v in node.items():
            yield from claims(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from claims(v, f"{path}[{i}]")


def main(argv) -> int:
    show_all = "--all" in argv
    todo_total = found_total = untagged = 0
    files = sorted(f for d in DIRS if d.exists() for f in d.glob("*.json"))

    for path in files:
        doc = json.loads(path.read_text(encoding="utf-8"))
        todos, findings, missing = [], [], []
        for where, claim in claims(doc):
            if claim["confidence"] != "unverified":
                continue
            flag = claim.get("search_exhausted")
            if flag is None:
                missing.append(where)
            elif flag:
                findings.append(where)
            else:
                todos.append(where)

        todo_total += len(todos)
        found_total += len(findings)
        untagged += len(missing)

        if todos or missing or (show_all and findings):
            print(f"\n{doc['id']}")
        for w in missing:
            print(f"    [UNTAGGED] {w}  — set search_exhausted")
        for w in todos:
            print(f"    [TODO]     {w}")
        if show_all:
            for w in findings:
                print(f"    [finding]  {w}")

    print(f"\n{'=' * 60}")
    print(f"Research todos:        {todo_total}")
    print(f"Established absences:  {found_total}")
    if untagged:
        print(f"Untagged (fix these):  {untagged}")
    print(f"Records:               {len(files)}")
    if todo_total:
        print("\nEach TODO is a field where the record does not yet know whether a")
        print("source exists. Closing one is a real contribution; so is flipping it")
        print("to search_exhausted: true with a note saying what was searched.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
