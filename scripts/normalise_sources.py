#!/usr/bin/env python3
"""Normalise citation strings across profiles so the same work is cited identically.

A work cited three slightly different ways appears three times in the generated
bibliography and cannot be counted, deduplicated, or checked for independence.
Per-use detail (which passage, which point it supports) belongs in the source's
`note` field, not in the citation string.

Run after editing profiles by hand:
    python3 scripts/normalise_sources.py
"""

from __future__ import annotations

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATASET = ROOT / "dataset"
CASES = ROOT / "cases"

# Canonical form for each work. Matching is by a distinctive substring.
CANONICAL = [
    (r"Bundy v\. State, 471 So\. ?2d 9",
     "Bundy v. State, 471 So. 2d 9 (Fla. 1985)"),
    (r"Bundy v\. State, 455 So\. ?2d 330",
     "Bundy v. State, 455 So. 2d 330 (Fla. 1984)"),
    (r"Bundy v\. Dugger, 850 F\. ?2d 1402",
     "Bundy v. Dugger, 850 F.2d 1402 (11th Cir. 1988)"),
    (r"Stranger Beside Me",
     "Rule, Ann. The Stranger Beside Me. New York: W. W. Norton, 1980."),
    (r"Bundy Murders",
     "Sullivan, Kevin M. The Bundy Murders: A Comprehensive History. Jefferson NC: McFarland, 2009."),
    (r"Only Living Witness",
     "Michaud, Stephen G. and Hugh Aynesworth. The Only Living Witness. New York: Simon & Schuster, 1983."),
    (r"\bRiverman\b",
     "Keppel, Robert D. and William J. Birnes. The Riverman: Ted Bundy and I Hunt for the Green River Killer. New York: Pocket Books, 1995."),
    (r"Environmental Range of Serial Rapists",
     "Canter, David and Paul Larkin. 'The Environmental Range of Serial Rapists.' Journal of Environmental Psychology 13(1), 1993, 63-69."),
    (r"Reduction of Linkage Blindness",
     "Egger, Steven A. 'A Working Definition of Serial Murder and the Reduction of Linkage Blindness.' Journal of Police Science and Administration 12(3), 1984, 348-357."),
    (r"Strengthening Forensic Science",
     "National Research Council. Strengthening Forensic Science in the United States: A Path Forward. Washington DC: National Academies Press, 2009."),
    (r"President's Council of Advisors",
     "President's Council of Advisors on Science and Technology. Forensic Science in Criminal Courts: Ensuring Scientific Validity of Feature-Comparison Methods. Washington DC, 2016."),
    (r"Innocence Project",
     "Innocence Project. 'In a Landmark Decision, Texas Forensic Science Commission Issues Moratorium on the Use of Bite Mark Evidence.' 2016."),
]


def split_multi(sources: list) -> list:
    """A citation naming two cases is two sources, not one."""
    out = []
    for src in sources:
        cit = src.get("citation", "")
        if cit.count(";") and re.search(r"\d+ (?:So|F)\.\s?2?d? \d+.*;.*\d+ (?:So|F)\.\s?2?d? \d+", cit):
            for part in cit.split(";"):
                clone = dict(src)
                clone["citation"] = part.strip()
                out.append(clone)
        else:
            out.append(src)
    return out


def canonicalise(src: dict) -> dict:
    cit = src.get("citation", "")
    for pattern, canonical in CANONICAL:
        if re.search(pattern, cit, re.I):
            # Preserve any trailing per-use gloss as a note.
            gloss = ""
            m = re.search(r"—\s*(.+)$", cit)
            if m:
                gloss = m.group(1).strip()
            else:
                m = re.search(r",\s*(ch\.\s*\d+|pp?\.\s*[\d-]+)\s*\.?$", cit, re.I)
                if m:
                    src["page"] = m.group(1)
            if gloss and not src.get("note"):
                src["note"] = gloss
            src["citation"] = canonical
            return src
    return src


def walk(node):
    if isinstance(node, dict):
        if "sources" in node and isinstance(node["sources"], list):
            node["sources"] = [canonicalise(s) for s in split_multi(node["sources"])]
        for v in node.values():
            walk(v)
    elif isinstance(node, list):
        for v in node:
            walk(v)


def main() -> int:
    for path in sorted(DATASET.glob("*.json")) + sorted(CASES.glob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        before = json.dumps(doc, sort_keys=True)
        walk(doc)
        after = json.dumps(doc, sort_keys=True)
        if before != after:
            path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"  normalised  {path.name}")
        else:
            print(f"  unchanged   {path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
