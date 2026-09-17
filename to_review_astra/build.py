#!/usr/bin/env python3
"""Build PDFs for unrefereed GPT-6 Astra would-publish resolutions.

Selection:
  model == gpt-6-astra
  would_publish == true
  verdict in {proved, disproved}

Unlike ``to_review/build.py``, this collection has not passed an adversarial
referee.  The PDFs therefore preserve the model writeup verbatim and label it
prominently as an unverified candidate result.

Usage: python3 to_review_astra/build.py [--only ID ...] [--no-pdf]
Requires: pandoc (or pypandoc_binary), latexmk, lualatex.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
LEGS = (
    ("attacks_opg", "OpenProblemGarden first pass"),
    ("attacks_arxiv_astra", "previously unattacked arXiv records"),
    ("attacks_retry", "selected second attempts"),
)
KEEP = {"proved", "disproved"}


def pandoc_bin() -> str | None:
    try:
        import pypandoc

        return pypandoc.get_pandoc_path()
    except Exception:
        return shutil.which("pandoc")


def yq(value: str) -> str:
    return "'" + value.replace("'", "''").replace("\n", " ") + "'"


def unlink(value: str) -> str:
    return re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", value)


def esc(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def shift_headings(md: str, by: int, drop_first_h1: bool = False) -> str:
    out: list[str] = []
    in_code = False
    dropped = False
    for line in md.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        match = re.match(r"^(#{1,6})\s", line)
        if match and not in_code:
            if drop_first_h1 and not dropped and len(match.group(1)) == 1:
                dropped = True
                continue
            line = "#" * by + line
        out.append(line)
    return "\n".join(out) + "\n"


def split_writeup(text: str) -> tuple[dict, str]:
    match = re.match(r"\s*```json\s*\n(.*?)\n```\s*\n", text, re.DOTALL)
    if not match:
        return {}, text
    try:
        claim = json.loads(match.group(1))
    except json.JSONDecodeError:
        claim = {}
    return claim, text[match.end() :]


def normalize_math_delimiters(text: str) -> str:
    """Make catalog-style ``$ x $`` spans valid Pandoc inline math."""
    return re.sub(
        r"(?<!\$)\$\s+([^$\n]*?\S)\s+\$(?!\$)",
        lambda match: f"${match.group(1)}$",
        text,
    )


def repair_tex(text: str) -> str:
    """Repair a few mechanical TeX defects present in the source artifacts."""
    text = text.replace("∎", r"\(\square\)")
    text = re.sub(r"\\mathb\s+([A-Za-z])", r"\\mathbb{\1}", text)

    def close_math_environments(match: re.Match) -> str:
        body = match.group(1)
        has_inner_environment = any(
            f"\\begin{{{env}}}" in body for env in ("aligned", "gathered", "split")
        )
        if not has_inner_environment:
            return match.group(0)
        for env in ("aligned", "gathered", "split"):
            missing = body.count(f"\\begin{{{env}}}") - body.count(f"\\end{{{env}}}")
            if missing > 0:
                body += "\n" + f"\\end{{{env}}}" * missing
        body = re.sub(r"\n\s*\n(?=\\end\{(?:aligned|gathered|split)\})", "\n", body)
        return "\\begin{equation*}\n" + body.strip() + "\n\\end{equation*}"

    return re.sub(r"\\\[(.*?)\\\]", close_math_environments, text, flags=re.DOTALL)


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return value[:70].rstrip("-") or "result"


def load_entries() -> list[dict]:
    entries: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for dirname, leg in LEGS:
        root = ROOT / dirname
        for verdict_path in sorted(root.glob("*/verdict.json")):
            verdict = json.loads(verdict_path.read_text())
            if (
                verdict.get("model") != "gpt-6-astra"
                or not verdict.get("would_publish")
                or verdict.get("verdict") not in KEEP
            ):
                continue
            cid = verdict_path.parent.name
            key = (dirname, cid)
            if key in seen:
                raise RuntimeError(f"duplicate Astra artifact: {dirname}/{cid}")
            seen.add(key)
            meta = json.loads((verdict_path.parent / "meta.json").read_text())
            entries.append(
                {
                    "id": cid,
                    "dirname": dirname,
                    "leg": leg,
                    "artifact": verdict_path.parent,
                    "verdict": verdict,
                    "meta": meta,
                }
            )
    return entries


def entry_title(entry: dict) -> str:
    meta = entry["meta"]
    dm = meta.get("dossier_meta", {})
    rec = meta.get("record", {})
    return unlink(dm.get("catalog_title") or rec.get("title_md") or entry["id"])


def pdf_name(entry: dict) -> str:
    return f"{entry['id']}__{slugify(entry_title(entry))}__astra-writeup.pdf"


def build_markdown(entry: dict) -> str:
    cid = entry["id"]
    meta = entry["meta"]
    verdict = entry["verdict"]
    dm = meta.get("dossier_meta", {})
    rec = meta.get("record", {})
    embedded_claim, body = split_writeup((entry["artifact"] / "output.md").read_text())
    body = repair_tex(normalize_math_delimiters(body))
    # Some model outputs place \tag inside an ``aligned`` block, which amsmath
    # rejects. Preserve the visible equation number without changing the formula.
    body = re.sub(r"\\tag\{([^{}]+)\}", r"\\qquad\\text{(\1)}", body)

    title = entry_title(entry)
    paper = dm.get("paper") or rec.get("paper") or ""
    catalog_url = dm.get("url") or rec.get("url") or ""
    statement = repair_tex(normalize_math_delimiters((dm.get("statement_text") or "").strip()))
    context = (dm.get("context_text") or "").strip().replace("\\item", "\n\n-")
    context = repair_tex(normalize_math_delimiters(context))
    source = rec.get("source") or meta.get("corpus") or ""
    arxiv_id = dm.get("arxiv_id")
    started = (meta.get("started") or "")[:10]
    one_line = verdict.get("one_line") or embedded_claim.get("one_line") or ""
    caveats = verdict.get("caveats") or embedded_claim.get("caveats") or ""
    verdict_word = "proof" if verdict["verdict"] == "proved" else "disproof"

    lines = [
        "---",
        f"title: {yq(title)}",
        f"subtitle: {yq(f'Unrefereed candidate {verdict_word} by GPT-6 Astra')}",
        "author:",
        f"  - {yq('Writeup: `gpt-6-astra` (single model pass)')}",
        f"date: {yq(f'Catalog id `{cid}` — generated {started}')}",
        "---",
        "",
        "::: {.warning}",
        "**UNREFEREED MODEL OUTPUT.** This document was selected solely because GPT-6 "
        "Astra labelled its own result `would_publish: true` and returned `proved` or "
        "`disproved`. It has not passed the adversarial LLM referee used for the earlier "
        "Sol campaign, has not been checked by a human mathematician, and has not been "
        "checked for novelty. Treat every mathematical and bibliographic claim below as "
        "unverified.",
        ":::",
        "",
        "# Summary and provenance",
        "",
        "| | |",
        "|:--|:--|",
        f"| Catalog id | `{cid}` |",
        f"| Catalog entry | [{esc(title)}]({catalog_url}) |",
        f"| Source corpus | {esc(source)} |",
        f"| Campaign leg | {esc(entry['leg'])} (`{entry['dirname']}`) |",
        f"| Source paper / entry | {esc(paper)} |",
        f"| Model verdict | **{verdict['verdict']}** (confidence: {esc(str(verdict.get('confidence', '?')))}) |",
        f"| Model's one-line claim | {esc(one_line)} |",
        f"| Model | `gpt-6-astra`, reasoning effort `max`, `mode=pro`, flex service tier |",
        f"| Original artifact | `{entry['dirname']}/{cid}/output.md` |",
        f"| Independent review | **None** |",
    ]
    if arxiv_id:
        lines.append(f"| arXiv | [arXiv:{arxiv_id}](https://arxiv.org/abs/{arxiv_id}) |")
    if caveats:
        lines.append(f"| Model's caveats | {esc(caveats)} |")
    lines.extend(
        [
            "",
            "# Problem statement",
            "",
            statement or "*No extracted statement was stored in the artifact metadata.*",
            "",
        ]
    )
    if context:
        lines.extend(["## Catalog context", "", context, ""])
    lines.extend(
        [
            "# Astra writeup",
            "",
            "*The text below is the model output verbatim, apart from moving its "
            "machine-readable verdict block into the summary above and shifting Markdown "
            "heading levels for this document. Mechanical TeX defects and equation tags "
            "were normalized where needed for compilation.*",
            "",
            shift_headings(body, 1),
        ]
    )
    return "\n".join(lines)


HEADER_TEX = r"""
\providecommand{\E}{\mathbb{E}}
\providecommand{\N}{\mathbb{N}}
\providecommand{\Z}{\mathbb{Z}}
\providecommand{\R}{\mathbb{R}}
\providecommand{\eps}{\varepsilon}
\providecommand{\ceil}[1]{\left\lceil #1\right\rceil}
\providecommand{\floor}[1]{\left\lfloor #1\right\rfloor}
\AtBeginDocument{\let\setminus\smallsetminus}
\usepackage[most]{tcolorbox}
\newtcolorbox{warning}{colback=red!5,colframe=red!65!black,boxrule=0.8pt,arc=2pt,left=6pt,right=6pt,top=5pt,bottom=5pt}
\usepackage{etoolbox}
\AtBeginEnvironment{longtable}{\small}
\setlength{\emergencystretch}{3em}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\bfseries UNREFEREED GPT-6 ASTRA OUTPUT}
\fancyhead[R]{\small\thepage}
\renewcommand{\headrulewidth}{0.4pt}
"""


LUA_FILTER = r"""
function Div(el)
  if el.classes:includes('warning') then
    return { pandoc.RawBlock('latex', '\\begin{warning}') } .. el.content .. { pandoc.RawBlock('latex', '\\end{warning}') }
  end
end
"""


def build_pdf(entry: dict, md_path: Path, outdir: Path) -> bool:
    pandoc = pandoc_bin()
    if not pandoc:
        print("pandoc not found; install pandoc or pypandoc_binary", file=sys.stderr)
        return False
    build = outdir / ".build"
    build.mkdir(exist_ok=True)
    header = build / "header.tex"
    lua = build / "warning.lua"
    header.write_text(HEADER_TEX)
    lua.write_text(LUA_FILTER)
    tex = outdir / f"{entry['id']}.tex"
    cmd = [
        pandoc,
        str(md_path),
        "-f",
        "markdown+tex_math_single_backslash+raw_tex",
        "-t",
        "latex",
        "--standalone",
        "--pdf-engine=lualatex",
        "-H",
        str(header),
        "--lua-filter",
        str(lua),
        "-V",
        "mainfont=Libertinus Serif",
        "-V",
        "mathfont=Latin Modern Math",
        "-V",
        "monofont=Latin Modern Mono",
        "-V",
        "monofontoptions=Scale=0.85",
        "-V",
        "fontsize=10pt",
        "-V",
        "geometry:margin=2.4cm",
        "-V",
        "colorlinks=true",
        "-V",
        "linkcolor=blue!50!black",
        "-V",
        "urlcolor=blue!50!black",
        "-o",
        str(tex),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode:
        print(f"[{entry['id']}] pandoc failed:\n{result.stderr}", file=sys.stderr)
        return False
    texmf_cache = HERE / ".build" / "texmf-var"
    texmf_cache.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [
            "latexmk",
            "-g",
            "-lualatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-outdir=.build",
            tex.name,
        ],
        cwd=outdir,
        capture_output=True,
        text=True,
        env={
            **os.environ,
            "TEXMFVAR": str(texmf_cache),
            "TEXMFCACHE": str(texmf_cache),
        },
    )
    log = build / f"{entry['id']}.log"
    if result.returncode:
        errors = []
        if log.exists():
            errors = [line for line in log.read_text(errors="replace").splitlines() if line.startswith("!")][:8]
        print(f"[{entry['id']}] latexmk failed: {errors}", file=sys.stderr)
        return False
    shutil.copy(build / f"{entry['id']}.pdf", HERE / pdf_name(entry))
    return True


def write_index(entries: list[dict], built: dict[tuple[str, str], bool]) -> None:
    rows = []
    for entry in sorted(entries, key=lambda item: (item["dirname"], item["id"])):
        cid = entry["id"]
        verdict = entry["verdict"]
        dm = entry["meta"].get("dossier_meta", {})
        rec = entry["meta"].get("record", {})
        url = dm.get("url") or rec.get("url") or ""
        name = pdf_name(entry)
        pdf = f"[{name}]({name})" if built.get((entry["dirname"], cid)) else "**build failed**"
        rows.append(
            f"| [`{cid}`]({url}) | {esc(entry_title(entry))} | {verdict['verdict']} | "
            f"{entry['leg']} | {esc(verdict.get('one_line', ''))} | {pdf} |"
        )
    proved = sum(entry["verdict"]["verdict"] == "proved" for entry in entries)
    disproved = len(entries) - proved
    text = f"""# Unrefereed Astra candidate results

This directory contains the **{len(entries)} GPT-6 Astra outputs** that the model
labelled `would_publish: true` with verdict `proved` ({proved}) or `disproved`
({disproved}). The four `would_publish` partial results are intentionally excluded.

These PDFs are assembled candidate writeups, not validated mathematical notes. They
preserve the Astra output and add the extracted problem statement, provenance, and a
prominent warning. **None has passed the adversarial referee stage, human review, a
novelty check, or formal verification.** The model's `would_publish` flag is only a
self-assessment.

Regenerate the collection with:

```bash
python3 to_review_astra/build.py
```

Generated Markdown and LaTeX sources are under `src/<id>/`.

## Candidate writeups

| id | problem | claim | campaign leg | model summary | pdf |
|:--|:--|:--|:--|:--|:--|
""" + "\n".join(rows) + "\n"
    (HERE / "README.md").write_text(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", nargs="*", default=None)
    parser.add_argument("--no-pdf", action="store_true")
    args = parser.parse_args()

    entries = load_entries()
    if len(entries) != 27:
        raise SystemExit(f"expected 27 Astra would-publish resolutions, found {len(entries)}")
    todo = [entry for entry in entries if not args.only or entry["id"] in args.only]
    built: dict[tuple[str, str], bool] = {}
    for entry in todo:
        cid = entry["id"]
        outdir = SRC / cid
        outdir.mkdir(parents=True, exist_ok=True)
        md_path = outdir / f"{cid}.md"
        md_path.write_text(build_markdown(entry))
        key = (entry["dirname"], cid)
        built[key] = (HERE / pdf_name(entry)).exists() if args.no_pdf else build_pdf(entry, md_path, outdir)
        print(f"[{cid}] {'ok' if built[key] else 'FAILED'}")
    for entry in entries:
        key = (entry["dirname"], entry["id"])
        built.setdefault(key, (HERE / pdf_name(entry)).exists())
    write_index(entries, built)
    if not args.no_pdf and not all(built[(entry["dirname"], entry["id"])] for entry in todo):
        raise SystemExit("one or more PDFs failed to build")


if __name__ == "__main__":
    main()
