#!/usr/bin/env python3
"""Build referee-ready PDFs for the surviving would_publish claims into to_review/.

Selection (from verification/verdicts.json):
  claimed_would_publish == True  and  review_verdict in {CONFIRMED, MINOR_GAPS}
i.e. the model itself flagged the result as publishable, and the adversarial
referee pass found it correct (possibly modulo routine repairable details) and not
already in the literature.

Layout:
  to_review/<id>__<slug>__note.pdf      hand-rewritten self-contained note (src/<id>/note.tex)
  to_review/<id>__<slug>__writeup.pdf   verbatim model writeup + referee report (pandoc)
  to_review/src/<id>/                   sources and .build/ for that id
  to_review/README.md                   index (regenerated)

Usage: python3 to_review/build.py [--only ID ...] [--no-pdf]
Requires: pandoc (pip install pypandoc_binary provides one), latexmk, lualatex.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
ATTACKS = ROOT / "attacks"
VERIF = ROOT / "verification"

KEEP = {"CONFIRMED", "MINOR_GAPS"}

SRC = HERE / "src"

# Descriptive file-name slugs (id -> slug).
SLUGS = {
    "1611.03196__03": "fair-representation-matchings-bipartite-c-of-m-bound",
    "1702.01094__01": "stable-set-covers-no-privately-covered-induced-path",
    "1812.02420__02": "fractional-dichromatic-number-2-NP-complete",
    "1812.02420__03": "directed-Kneser-graphs-acyclic-iff-intersecting",
    "1902.10878__01": "concatenating-bipartite-graphs-psi-not-symmetric",
    "2103.15175__00": "multicolor-list-Ramsey-number-equals-s-to-the-k-plus-1",
    "2208.06858__01": "Levine-hat-problem-monotone-strategies-reach-one-half",
    "2310.04265__09": "3-critical-tournaments-clique-number-question-5.9",
    "2401.00299__02": "hypercube-partitions-into-squares-asymptotics",
    "2405.03455__00": "Erdos-Szekeres-big-line-or-big-convex-polygon-linear-in-l",
    "2408.02400__00": "chromatic-minus-cochromatic-number-Mycielski-construction",
    "2512.10438__00": "color-avoiding-paths-tournaments-q6-N9-example",
    "2001.09679__00": "sublinear-separators-expansion-exponent-Dvorak-b-eps",
    "2005.09767__00": "group-connectivity-exponentially-many-flows-Z6-Z7",
    "2211.01032__02": "random-embeddings-expected-faces-Theta-log-n",
    "2505.24100__01": "induced-saturation-even-cycles-line-graphs-hypohamiltonian",
}


def pdf_name(cid: str) -> str:
    kind = "note" if (SRC / cid / "note.tex").exists() else "writeup"
    return f"{cid}__{SLUGS.get(cid, 'result')}__{kind}.pdf"


def pandoc_bin():
    try:
        import pypandoc
        return pypandoc.get_pandoc_path()
    except Exception:
        return shutil.which("pandoc")


def shift_headings(md: str, by: int, drop_first_h1: bool = False) -> str:
    out, in_code, dropped = [], False, False
    for line in md.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        m = re.match(r"^(#{1,6})\s", line)
        if m and not in_code:
            if drop_first_h1 and not dropped and len(m.group(1)) == 1:
                dropped = True
                continue
            line = "#" * by + line
        out.append(line)
    return "\n".join(out) + "\n"


def split_writeup(text: str):
    """Return (claimed_json_dict, body) from attacks/<id>/output.md."""
    m = re.match(r"\s*```json\s*\n(.*?)\n```\s*\n", text, re.DOTALL)
    if not m:
        return {}, text
    try:
        claimed = json.loads(m.group(1))
    except json.JSONDecodeError:
        claimed = {}
    return claimed, text[m.end():]


def strip_yaml(text: str):
    m = re.match(r"\s*---\n(.*?)\n---\n", text, re.DOTALL)
    return (m.group(1), text[m.end():]) if m else ("", text)


def yaml_field(header: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.*)$", header, re.M)
    return m.group(1).strip() if m else ""


def yq(s: str) -> str:
    """Single-quoted YAML scalar (no backslash escapes are interpreted)."""
    return "'" + s.replace("'", "''").replace("\n", " ") + "'"


def unlink(s: str) -> str:
    """Strip markdown links [text](url) -> text."""
    return re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)


def esc(s: str) -> str:
    """Escape pipe characters for use inside a pipe-table cell."""
    return s.replace("|", "\\|").replace("\n", " ")


def build_markdown(e: dict) -> str:
    cid = e["id"]
    meta = json.loads((ATTACKS / cid / "meta.json").read_text())
    dm = meta.get("dossier_meta", {})
    rec = meta.get("record", {})
    claimed, body = split_writeup((ATTACKS / cid / "output.md").read_text())
    rheader, rbody = strip_yaml((VERIF / f"{cid}.md").read_text())
    # the referee agents ran on another machine; make paths repo-relative
    rbody = rbody.replace("/Users/viennot/dev/Graph-Theory-LLM-Proofs/", "")
    # a "- item" line glued to a text line is a paragraph in Markdown; make it a list
    rbody = re.sub(r"(?m)^(?![-*\s]|$)(.+)\n(?=[-*] )", r"\1\n\n", rbody)

    arxiv = dm.get("arxiv_id", cid.split("__")[0])
    paper = dm.get("paper") or rec.get("paper", "")
    ctitle = unlink(dm.get("catalog_title") or rec.get("title_md", cid))
    url = dm.get("url") or rec.get("url", "")
    model = meta.get("model", "?")
    effort = meta.get("reasoning", {}).get("effort", "")
    started = meta.get("started", "")[:10]
    claim = e["claimed_verdict"]
    verdict_word = {"proved": "Proof", "disproved": "Disproof"}.get(claim, "Resolution")

    title = f"{ctitle} of arXiv:{arxiv}"
    subtitle = f"Candidate {verdict_word.lower()} — {paper}"

    lines = []
    lines.append("---")
    lines.append(f"title: {yq(title)}")
    lines.append(f"subtitle: {yq(subtitle)}")
    lines.append("author:")
    lines.append("  - " + yq(f"Writeup: `{model}` (single pass, {started})"))
    lines.append("  - " + yq(f"Adversarial referee: `{e.get('review_model', 'claude-fable-5')}` — verdict **{e['review_verdict']}**"))
    lines.append("date: " + yq(f"Catalog id `{cid}`"))
    lines.append("---")
    lines.append("")
    lines.append("::: {.callout}")
    lines.append("**How to read this document.** The proof below was written autonomously by a "
                 "large language model in a single pass, then checked by an independent LLM "
                 "referee instructed to assume it wrong (re-deriving every step, fetching every "
                 "cited source, and brute-forcing every finite object). Neither step involved a "
                 "human mathematician. We are circulating it precisely to obtain an expert "
                 "opinion: is the argument correct, and is the result new? The LLM referee "
                 "report is reproduced in the appendix for convenience; please do not treat it "
                 "as authoritative.")
    lines.append(":::")
    lines.append("")
    lines.append("# Summary")
    lines.append("")
    lines.append("| | |")
    lines.append("|:--|:--|")
    lines.append(f"| Source paper | *{esc(paper)}*, [arXiv:{arxiv}](https://arxiv.org/abs/{arxiv}) |")
    lines.append(f"| Catalog entry | [{esc(ctitle)}]({url}) (id `{cid}`) |")
    lines.append(f"| Claimed verdict | **{claim}** (model confidence: {claimed.get('confidence', e.get('claimed_confidence', '?'))}) |")
    lines.append(f"| Claim in one line | {esc(claimed.get('one_line', e.get('claimed_one_line', '')))} |")
    if claimed.get("caveats"):
        lines.append(f"| Writeup's own caveats | {esc(claimed['caveats'])} |")
    lines.append(f"| Writeup model | `{model}`" + (f" (reasoning effort: {effort})" if effort else "") + f", {started} |")
    lines.append(f"| Referee verdict | **{e['review_verdict']}** (confidence: {yaml_field(rheader, 'confidence')}; "
                 f"interpretation ok: {yaml_field(rheader, 'interpretation_ok')}; references ok: {yaml_field(rheader, 'references_ok')}; "
                 f"computation run: {yaml_field(rheader, 'computation_run')}) |")
    lines.append(f"| Referee in one line | {esc(yaml_field(rheader, 'one_line'))} |")
    lines.append("")
    lines.append("# Problem statement")
    lines.append("")
    lines.append(f"**{esc(ctitle)}** (from *{esc(paper)}*, arXiv:{arxiv}; catalog wording).")
    lines.append("")
    lines.append(dm.get("statement_text", "").strip())
    lines.append("")
    if dm.get("context_text"):
        lines.append(f"*Context.* {dm['context_text'].strip()}")
        lines.append("")
    lines.append("# The writeup")
    lines.append("")
    lines.append(f"*Verbatim output of `{model}`; only the machine-readable verdict block has been moved to the summary table above.*")
    lines.append("")
    lines.append(shift_headings(body, 1))
    lines.append("")
    lines.append("\\appendix")
    lines.append("")
    lines.append("# Referee report (LLM-generated)")
    lines.append("")
    lines.append(f"*Verbatim report of the adversarial referee agent (`{e.get('review_model', 'claude-fable-5')}`), "
                 f"file `verification/{cid}.md`. Scripts used for the computational checks are in "
                 f"`verification/scripts/{cid}/`.*")
    lines.append("")
    lines.append(shift_headings(rbody, 0, drop_first_h1=True))
    return "\n".join(lines)


HEADER_TEX = r"""
\providecommand{\E}{\mathbb{E}}
\providecommand{\N}{\mathbb{N}}
\providecommand{\Z}{\mathbb{Z}}
\providecommand{\R}{\mathbb{R}}
\providecommand{\eps}{\varepsilon}
% glyphs missing from Libertinus (combining vector arrow, script letters, long arrows): fall back
\directlua{luaotfload.add_fallback("cfb", {"NotoSansMath:mode=harf;", "DejaVuSans:mode=harf;"})}
\setmainfont{Libertinus Serif}[RawFeature={fallback=cfb}]
% Latin Modern Math lacks U+29F5 (unicode-math's \setminus); use the small variant
\AtBeginDocument{\let\setminus\smallsetminus}
\usepackage{tcolorbox}
\newtcolorbox{callout}{colback=gray!8,colframe=gray!50,boxrule=0.4pt,arc=2pt,left=6pt,right=6pt,top=4pt,bottom=4pt}
\usepackage{etoolbox}
\AtBeginEnvironment{longtable}{\small}
\setlength{\emergencystretch}{3em}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\itshape Candidate result — LLM-generated, awaiting human review}
\fancyhead[R]{\small\thepage}
\renewcommand{\headrulewidth}{0.2pt}
"""

# pandoc renders ::: {.callout} as \begin{callout}...\end{callout} via this filter-free trick:
LUA_FILTER = r"""
function Div(el)
  if el.classes:includes('callout') then
    return { pandoc.RawBlock('latex', '\\begin{callout}') } .. el.content .. { pandoc.RawBlock('latex', '\\end{callout}') }
  end
end
"""


def referee_fragment(cid: str, outdir: Path) -> Path:
    """Convert verification/<id>.md (minus YAML header and title) into a LaTeX fragment."""
    rheader, rbody = strip_yaml((VERIF / f"{cid}.md").read_text())
    rbody = rbody.replace("/Users/viennot/dev/Graph-Theory-LLM-Proofs/", "")
    rbody = re.sub(r"(?m)^(?![-*\s]|$)(.+)\n(?=[-*] )", r"\1\n\n", rbody)
    rbody = shift_headings(rbody, 0, drop_first_h1=True)
    # long inline formulas in the referee's prose cannot break across lines; allow breaks after commas
    brk = lambda t: t.replace(",", ",\\allowbreak ")
    rbody = re.sub(r"\$([^$\n]{35,})\$", lambda m: "$" + brk(m.group(1)) + "$", rbody)
    rbody = re.sub(r"\\\(([^\n]{35,}?)\\\)", lambda m: "\\(" + brk(m.group(1)) + "\\)", rbody)
    build = outdir / ".build"
    build.mkdir(exist_ok=True)
    md = build / "referee.md"
    md.write_text(rbody)
    tex = build / "referee.tex"
    r = subprocess.run([pandoc_bin(), str(md), "-f", "markdown+tex_math_single_backslash", "-t", "latex",
                        "--top-level-division=section", "-o", str(tex)], capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f"[{cid}] pandoc (referee fragment) failed:\n{r.stderr}")
    return tex


def build_note_pdf(cid: str, outdir: Path) -> bool:
    """Compile a hand-written note.tex (which \\inputs .build/referee.tex) into <id>.pdf."""
    try:
        referee_fragment(cid, outdir)
    except RuntimeError as err:
        print(err, file=sys.stderr)
        return False
    r = subprocess.run(["latexmk", "-lualatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-outdir=.build", "note.tex"], cwd=outdir, capture_output=True, text=True)
    log = outdir / ".build" / "note.log"
    if r.returncode:
        errs = [l for l in log.read_text(errors="replace").splitlines() if l.startswith("!")][:5] if log.exists() else []
        print(f"[{cid}] latexmk (note) failed: {errs}", file=sys.stderr)
        return False
    shutil.copy(outdir / ".build" / "note.pdf", HERE / pdf_name(cid))
    return True


def build_pdf(cid: str, md_path: Path, outdir: Path) -> bool:
    pandoc = pandoc_bin()
    if not pandoc:
        print("pandoc not found", file=sys.stderr)
        return False
    header = outdir / ".build" / "header.tex"
    lua = outdir / ".build" / "callout.lua"
    header.parent.mkdir(exist_ok=True)
    header.write_text(HEADER_TEX)
    lua.write_text(LUA_FILTER)
    tex = outdir / f"{cid}.tex"
    cmd = [pandoc, str(md_path), "-f", "markdown+tex_math_single_backslash", "-t", "latex", "--standalone",
           "--pdf-engine=lualatex", "-H", str(header), "--lua-filter", str(lua),
           "-V", "mainfont=Libertinus Serif", "-V", "mathfont=Latin Modern Math",
           "-V", "monofont=Latin Modern Mono", "-V", "monofontoptions=Scale=0.85",
           "-V", "fontsize=11pt", "-V", "geometry:margin=2.6cm", "-V", "colorlinks=true",
           "-V", "linkcolor=blue!50!black", "-V", "urlcolor=blue!50!black",
           "-o", str(tex)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(f"[{cid}] pandoc failed:\n{r.stderr}", file=sys.stderr)
        return False
    r = subprocess.run(["latexmk", "-lualatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-outdir=.build", tex.name], cwd=outdir, capture_output=True, text=True)
    log = outdir / ".build" / f"{cid}.log"
    if r.returncode:
        errs = [l for l in log.read_text(errors="replace").splitlines() if l.startswith("!")][:5] if log.exists() else []
        print(f"[{cid}] latexmk failed: {errs}", file=sys.stderr)
        return False
    shutil.copy(outdir / ".build" / f"{cid}.pdf", HERE / pdf_name(cid))
    return True


def write_index(entries, built):
    rows = []
    for e in sorted(entries, key=lambda e: (0 if e["review_verdict"] == "CONFIRMED" else 1, e["id"])):
        cid = e["id"]
        meta = json.loads((ATTACKS / cid / "meta.json").read_text())
        dm, rec = meta.get("dossier_meta", {}), meta.get("record", {})
        arxiv = dm.get("arxiv_id", cid.split("__")[0])
        ctitle = unlink(dm.get("catalog_title") or rec.get("title_md", ""))
        kind = "rewritten note" if (SRC / cid / "note.tex").exists() else "verbatim writeup"
        name = pdf_name(cid)
        pdf = f"[{name}]({name})" if built.get(cid) else "(build failed)"
        rows.append(f"| [`{cid}`]({dm.get('url', '')}) | {esc(ctitle)} | "
                    f"*{esc(dm.get('paper', ''))}* ([arXiv:{arxiv}](https://arxiv.org/abs/{arxiv})) | "
                    f"{e['claimed_verdict']} | {e['review_verdict']} | {kind} | {pdf} |")
    n_c = sum(e["review_verdict"] == "CONFIRMED" for e in entries)
    n_m = sum(e["review_verdict"] == "MINOR_GAPS" for e in entries)
    n_notes = sum((SRC / e["id"] / "note.tex").exists() for e in entries)
    text = f"""# Results to review

Claimed resolutions of open problems from the catalog that (a) the attacking model
itself flagged as `would_publish: true`, and (b) survived the adversarial referee pass
in `../verification/` with verdict **CONFIRMED** ({n_c}) or **MINOR_GAPS** ({n_m},
correct modulo routine repairable details), and were not found to be already in the
literature during that review. Total: {len(entries)}. Later literature updates below
do not change the recorded referee verdicts.

Two kinds of PDF, distinguished by the file-name suffix:

- `__note.pdf` ({n_notes}): a self-contained mathematical note rewritten from the model's
  writeup (statement, proof ideas, full proofs in Appendix A, the verbatim LLM referee
  report in Appendix B). Every deviation from the original writeup is declared in the
  provenance box on page 1. For the MINOR_GAPS items the gaps named by the referee were
  repaired in the rewrite, and each repair is marked where it occurs.
- `__writeup.pdf` ({len(entries) - n_notes}): the model's writeup verbatim, with a summary
  table, the problem statement and the referee report appended (none at present; this is
  what an id without a `src/<id>/note.tex` produces).

Sources are in `src/<id>/` (`note.tex` where a note exists). Regenerate everything with
`python3 to_review/build.py`.

**Caveat.** Nothing here has been checked by a human mathematician. "CONFIRMED" is the
verdict of an LLM referee, and novelty was checked only against the indexed literature.

## Literature updates

**2026-09-10: `2310.04265__09` overlaps with published work.** Samuel Coulomb
drew our attention to recent results. The same circulant family and its
clique-number criticality appear in [Aubian and Coulomb, result 6.1](https://arxiv.org/html/2609.07481#S6).
The general critical-tournament conjecture is settled by
[Chen and Wang, Theorem 1.1](https://arxiv.org/html/2609.08658).
The note is retained as an account of a machine-generated proof, not as a claim to
a new resolution. Its recorded generation date is 2026-09-01; the Aubian-Coulomb
preprint was submitted on 2026-09-07. These dates do not establish priority or
independent discovery. The note's related-work discussion has been updated, while
the original proof and referee report are preserved. This update does not assess
the novelty of the other notes.

## Notes

| id | problem | source paper | claim | referee | format | pdf |
|:--|:--|:--|:--|:--|:--|:--|
""" + "\n".join(rows) + "\n"
    (HERE / "README.md").write_text(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", default=None)
    ap.add_argument("--no-pdf", action="store_true")
    args = ap.parse_args()

    verdicts = json.loads((VERIF / "verdicts.json").read_text())["verdicts"]
    entries = [e for e in verdicts if e.get("claimed_would_publish") and e["review_verdict"] in KEEP]
    todo = [e for e in entries if not args.only or e["id"] in args.only]
    built = {}
    for e in todo:
        cid = e["id"]
        outdir = SRC / cid
        outdir.mkdir(parents=True, exist_ok=True)
        if args.no_pdf:
            built[cid] = (HERE / pdf_name(cid)).exists()
            continue
        # remove superseded outputs for this id (e.g. an old __writeup.pdf once a note exists)
        for stale in HERE.glob(f"{cid}__*.pdf"):
            if stale.name != pdf_name(cid):
                stale.unlink()
        if (outdir / "note.tex").exists():
            # a rewritten, self-contained note supersedes the assembled markdown
            for stale in (outdir / f"{cid}.md", outdir / f"{cid}.tex"):
                stale.unlink(missing_ok=True)
            built[cid] = build_note_pdf(cid, outdir)
        else:
            md_path = outdir / f"{cid}.md"
            md_path.write_text(build_markdown(e))
            built[cid] = build_pdf(cid, md_path, outdir)
        print(f"[{cid}] {'ok' if built[cid] else 'FAILED'}")
    # entries not rebuilt this run keep whatever pdf exists
    for e in entries:
        built.setdefault(e["id"], (HERE / pdf_name(e["id"])).exists())
    write_index(entries, built)


if __name__ == "__main__":
    main()
