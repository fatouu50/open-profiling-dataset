#!/usr/bin/env python3
"""Extract investigation.detection_delay_factors from every record.

docs/detection-mechanisms.md interprets these fields. This script prints the
underlying data so a reader can check the interpretation against the record
rather than taking it on trust — which is the same standard the dataset
applies to its sources.

Usage:
    python3 scripts/detection_table.py           # summary table
    python3 scripts/detection_table.py --full    # full field text and sources
"""

from __future__ import annotations

import json
import pathlib
import sys
import textwrap

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIRS = [ROOT / "dataset", ROOT / "cases"]


def main(argv) -> int:
    full = "--full" in argv
    files = sorted(f for d in DIRS if d.exists() for f in d.glob("*.json"))
    if not files:
        print("No records found.")
        return 0

    print(f"{'record':<20}  {'first':<12}{'last':<12}confidence")
    print("-" * 62)

    rows = []
    for path in files:
        doc = json.loads(path.read_text(encoding="utf-8"))
        inv = doc.get("investigation") or {}
        ddf = inv.get("detection_delay_factors")
        period = doc.get("offence_period") or {}
        first = (period.get("first_known_offence") or {}).get("value") or "—"
        last = (period.get("last_known_offence") or {}).get("value") or "—"
        conf = (ddf or {}).get("confidence", "—")
        rows.append((doc["id"], first, last, conf, ddf))
        print(f"{doc['id']:<20}  {str(first):<12}{str(last):<12}{conf}")

    if full:
        for rid, first, last, conf, ddf in rows:
            print(f"\n{'=' * 70}\n{rid}  ({conf})\n")
            if not ddf:
                print("  (no detection_delay_factors recorded)")
                continue
            print(textwrap.fill(str(ddf.get("value") or "—"), 70,
                                initial_indent="  ", subsequent_indent="  "))
            if ddf.get("notes"):
                print()
                print(textwrap.fill("NOTE: " + ddf["notes"], 70,
                                    initial_indent="  ", subsequent_indent="  "))
            for s in ddf.get("sources", []):
                print(f"\n  [tier {s.get('tier')}] {s.get('citation')}")

    print(f"\n{len(rows)} record(s). "
          "Run with --full for the field text and citations.")
    print("Interpretation of these fields is in docs/detection-mechanisms.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
