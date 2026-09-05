#!/usr/bin/env python3
"""Render dataset/<ID>.md from dataset/<ID>.json.

The Markdown report is a BUILD ARTEFACT. It is generated from the validated
JSON and must never be hand-edited: edits would be overwritten, and worse, a
hand-written report can assert things the JSON does not support. That is
precisely the failure this project exists to prevent.

Every rendered claim carries its confidence level and its sources inline.
A claim with no source cannot appear, because it does not exist in the JSON.

Usage:
    python3 scripts/render_md.py            # render all profiles
    python3 scripts/render_md.py --check    # verify .md files are in sync (CI)
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATASET = ROOT / "dataset"

BADGE = {
    "established": "**established**",
    "reported": "*reported*",
    "contested": "⚠︎ **contested**",
    "unverified": "○ *not established*",
}

SECTIONS = [
    ("identity", "Identity", None),
    ("conviction_record", "Conviction record",
     "The evidentiary spine. Every behavioural claim below rests on this; if this section is thin, the rest is speculation."),
    ("offence_period", "Offence period", None),
    ("background", "Background",
     "Childhood accounts in this literature rest heavily on retrospective self-report given after arrest. Confidence levels here should be read sceptically even where sources exist."),
    ("clinical", "Clinical",
     "Formal assessments only. Labels applied by commentators who never examined the subject appear under *commentary attributions* and are claims about the discourse, not about the person."),
    ("offence_behaviour", "Offence behaviour", None),
    ("investigation", "Investigation", None),
    ("adjudication", "Adjudication", None),
]

FIELD_NOTES = {
    "macdonald_triad": (
        "The Macdonald triad is recorded because the historical literature uses it and "
        "replication studies need it. **It is not a predictor of violence** — Parfitt & "
        "Alleyne (2020) found no support for it as one."
    ),
    "claimed_victim_count": (
        "Offender self-report. Recorded as a datum about what the subject said, "
        "never as a victim count."
    ),
    "method_now_disputed": (
        "A technique relied on at trial that has since been found scientifically unreliable."
    ),
    "commentary_attributions": (
        "Diagnostic labels applied in secondary literature by people who never examined "
        "the subject. Not diagnostic data."
    ),
}


def humanise(key: str) -> str:
    return key.replace("_", " ").capitalize()


def is_claim(node) -> bool:
    return isinstance(node, dict) and {"value", "confidence", "sources"} <= node.keys()


def fmt_value(value) -> str:
    if value is None:
        return "—"
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, list):
        if not value:
            return "—"
        if all(isinstance(v, dict) for v in value):
            out = []
            for item in value:
                parts = [f"**{k.replace('_', ' ')}:** {v}" for k, v in item.items()]
                out.append("  - " + "; ".join(parts))
            return "\n" + "\n".join(out)
        return "\n" + "\n".join(f"  - {v}" for v in value)
    return str(value)


def render_claim(key: str, claim: dict, sources_index: list, depth: int = 0) -> list[str]:
    lines = []
    pad = "  " * depth
    badge = BADGE.get(claim["confidence"], claim["confidence"])
    value = fmt_value(claim["value"])

    lines.append(f"{pad}**{humanise(key)}** — {badge}")
    lines.append("")
    if value.startswith("\n"):
        lines.append(value.strip("\n"))
    else:
        lines.append(f"{pad}{value}")
    lines.append("")

    # The index is keyed on the citation alone, so one work is one entry
    # however many times it is cited. Per-use detail (page, gloss) stays
    # with the reference, not in the bibliography.
    refs = []
    for src in claim.get("sources", []):
        citation = src.get("citation", "")
        key = next((k for k in sources_index if k[1] == citation), None)
        if key is None:
            key = (src.get("tier"), citation, src.get("url", ""))
            sources_index.append(key)
        ref = f"[{sources_index.index(key) + 1}"
        if src.get("page"):
            ref += f", {src['page']}"
        ref += "]"
        if src.get("note"):
            ref += f" *({src['note']})*"
        refs.append(ref)
    if refs:
        lines.append(f"{pad}Sources: {' '.join(refs)}")
        lines.append("")

    if claim.get("notes"):
        lines.append(f"{pad}> {claim['notes']}")
        lines.append("")

    return lines


def render_group(key: str, node: dict, sources_index: list) -> list[str]:
    lines = [f"#### {humanise(key)}", ""]
    if key in FIELD_NOTES:
        lines += [f"> {FIELD_NOTES[key]}", ""]
    for subkey, sub in node.items():
        if is_claim(sub):
            lines += render_claim(subkey, sub, sources_index)
        elif isinstance(sub, dict):
            lines += render_group(subkey, sub, sources_index)
    return lines


def render(doc: dict) -> str:
    sources_index: list = []
    body: list[str] = []

    for key, title, preamble in SECTIONS:
        node = doc.get(key)
        if not isinstance(node, dict) or not node:
            continue
        body += [f"## {title}", ""]
        if preamble:
            body += [f"> {preamble}", ""]
        for subkey, sub in node.items():
            if sub is None:
                continue
            if is_claim(sub):
                if subkey in FIELD_NOTES:
                    body += [f"> {FIELD_NOTES[subkey]}", ""]
                body += render_claim(subkey, sub, sources_index)
            elif isinstance(sub, dict):
                body += render_group(subkey, sub, sources_index)
        body += ["---", ""]

    ident = doc.get("identity", {})
    name = ident.get("legal_name", {}).get("value", doc["id"])
    prov = doc.get("provenance", {})

    head = [
        f"# {name}",
        "",
        f"`{doc['id']}` · record status: **{doc.get('record_status', 'unknown')}** · "
        f"schema {doc.get('schema_version', '?')}",
        "",
        "> **This file is generated.** It is rendered from "
        f"[`{doc['id']}.json`](./{doc['id']}.json) by `scripts/render_md.py`. "
        "Do not edit it by hand — edits are overwritten, and a hand-written report can "
        "assert what the data does not support. Change the JSON, then re-render.",
        "",
        "### How to read this",
        "",
        "Every claim carries a confidence level:",
        "",
        "| Level | Meaning |",
        "|---|---|",
        "| **established** | Two or more independent sources, at least one primary or peer-reviewed |",
        "| *reported* | A single credible source |",
        "| ⚠︎ **contested** | Credible sources disagree — see the note |",
        "| ○ *not established* | No admissible source found. The note says what was searched |",
        "",
        "A field showing **—** is not an oversight. It means no source was found, and the "
        "note records the attempt. Absence of evidence is recorded rather than filled in.",
        "",
        "---",
        "",
    ]

    tail: list[str] = []
    dq = doc.get("data_quality") or {}
    if dq:
        tail += ["## Data quality", ""]
        for field, title in [
            ("known_gaps", "What this record does not establish"),
            ("contested_points", "Contested points"),
            ("excluded_material", "Material deliberately excluded"),
        ]:
            items = dq.get(field)
            if items:
                tail += [f"### {title}", ""]
                tail += [f"- {i}" for i in items]
                tail += [""]
        tail += ["---", ""]

    if sources_index:
        tail += ["## Sources", "",
                 "Tier 1 = primary record · 2 = peer-reviewed · 3 = book-length journalism "
                 "with a sourcing apparatus · 4 = contemporaneous reporting. "
                 "Dramatisations, wikis and AI output are inadmissible at any tier.", ""]
        for i, (tier, citation, url) in enumerate(sources_index, 1):
            line = f"{i}. *(tier {tier})* {citation}"
            if url:
                line += f" — <{url}>"
            tail += [line]
        tail += [""]

    tail += [
        "---",
        "",
        "## Provenance",
        "",
        f"- Created: {prov.get('created', '?')}",
        f"- Last reviewed: {prov.get('last_reviewed', '?')}",
        f"- Contributors: {', '.join(prov.get('contributors', []))}",
        f"- AI-assisted drafting: **{'yes' if prov.get('ai_assisted') else 'no'}**"
        + ("  \n  Every claim was nonetheless verified against a human-readable source. "
           "AI output is never itself a source." if prov.get("ai_assisted") else ""),
        "",
        "See [`../ETHICS.md`](../ETHICS.md) for the constraints governing what this record "
        "may and may not contain, and [`../docs/sourcing-policy.md`](../docs/sourcing-policy.md) "
        "for source admissibility.",
        "",
    ]

    return "\n".join(head + body + tail).rstrip() + "\n"


def main(argv) -> int:
    check = "--check" in argv
    files = sorted(DATASET.glob("*.json"))
    if not files:
        print("No profiles found in dataset/.")
        return 0

    stale = []
    for path in files:
        doc = json.loads(path.read_text(encoding="utf-8"))
        out = path.with_suffix(".md")
        rendered = render(doc)

        if check:
            if not out.exists() or out.read_text(encoding="utf-8") != rendered:
                stale.append(out.name)
                print(f"  STALE  {out.name}")
            else:
                print(f"  ok     {out.name}")
        else:
            out.write_text(rendered, encoding="utf-8")
            print(f"  wrote  {out.name}  ({len(rendered.splitlines())} lines)")

    if check and stale:
        print(f"\n{len(stale)} file(s) out of sync. Run: python3 scripts/render_md.py")
        return 1
    print(f"\n{len(files)} profile(s) processed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
