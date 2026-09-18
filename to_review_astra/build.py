#!/usr/bin/env python3
"""Build referee-ready notes for the gpt-6-astra campaign's surviving claims.

Selection (from ../verification_astra/verdicts.json):
  review_verdict in {CONFIRMED, MINOR_GAPS}
i.e. the adversarial referee pass found the claim correct (possibly modulo routine
repairs) and not already in the literature. ALREADY_KNOWN claims are excluded, as in
../to_review/.

Layout (mirrors ../to_review/):
  to_review_astra/<id>__<slug>__note.pdf   self-contained note (src/<id>/note.tex)
  to_review_astra/src/<id>/                 note.tex and .build/ for that id
  to_review_astra/README.md                 index (regenerated)

Each note is compiled with lualatex; Appendix B is the verbatim referee report from
../verification_astra/<id>.md, converted with pandoc into .build/referee.tex.

Usage: python3 to_review_astra/build.py [--only ID ...] [--no-pdf]
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
SRC = HERE / "src"
VERIF = ROOT / "verification_astra"
CATALOG = ROOT / "catalog"

KEEP = {"CONFIRMED", "MINOR_GAPS"}
LEG_LABEL = {
    "attacks_opg": "OpenProblemGarden",
    "attacks_arxiv_astra": "arXiv, previously unattacked",
    "attacks_retry": "retry of a still-open problem",
}

# Descriptive file-name slugs (id -> slug).
SLUGS = {
    "1602.05184__00": "szeged-wiener-strengthening-eta-at-least-2n-for-2-connected",
    "1812.09215__00": "moore-type-bound-disproves-bijection-existence",
    "1904.02595__00": "tensor-rank-bound-retaining-lonely-vertices",
    "1912.01570__00": "planar-fvs-vs-feedback-path-number-12-vertex-counterexample",
    "2008.03587__00": "deterministic-zombies-waiting-helps-59-vertex-cactus",
    "2105.15195__00": "conlon-fox-pham-conjecture-10-constant-for-all-r",
    "2106.03261__00": "petersen-forcing-lemma-twisted-polarity-graph",
    "2106.03261__01": "asymptotically-regular-C4-free-petersen-free-construction",
    "2207.13651__00": "fox-luo-pham-random-subgraph-threshold-d-log-n",
    "2211.01032__03": "nonorientable-random-embeddings-expected-faces-ln-n",
    "2304.03567__03": "RFCPP-no-constant-factor-approximation-unless-P-equals-NP",
    "2506.08810__03": "five-vertex-tournament-counterexample-conjecture-24",
    "2507.10840__01": "plane-path-partition-number-odd-polygon-central-cluster",
    "2509.09031__00": "quasi-isometry-conjecture-contraction-closed-counterexample",
    "2603.02786__00": "AP-packing-all-differences-constant-4-3-prime-blocks",
    "2604.09449__03": "colour-balanced-hamilton-cycles-k-log-k",
    "a_generalization_of_vizings_theorem": "rosenfeld-hypergraph-vizing-disproof-100-uniform",
    "chromatic_number_of_random_lifts_of_complete_graphs": "random-lifts-of-K5-are-3-chromatic",
    "circular_colouring_the_orthogonality_graph": "orthogonality-graph-circular-chromatic-number-is-4",
    "covering_powers_of_cycles_with_equivalence_subgraphs": "equivalence-covering-powers-of-cycles-log-k",
    "geodesic_cycles_and_tuttes_theorem": "kleetope-of-K4-refutes-georgakopoulos-spruessel-problem-3",
    "melnikovs_valency_variety_problem": "melnikov-valency-variety-37-vertex-counterexample",
    "mixing_circular_colourings_0": "circular-mixing-threshold-rational-numerator-at-most-n-plus-1",
    "random_stable_roommates": "random-stable-roommates-solvability-n-to-minus-one-sixth",
}


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


def strip_yaml(text: str):
    m = re.match(r"\s*---\n(.*?)\n---\n", text, re.DOTALL)
    return (m.group(1), text[m.end():]) if m else ("", text)


def esc(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def unlink(s: str) -> str:
    return re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s or "")


# ---------------------------------------------------------------- catalog lookups
_ARXIV = None
_OPG = None


def arxiv_record(cid: str) -> dict:
    """catalog/arxiv_conjectures.json indexed like attack.py: <arxiv_id>__<NN>."""
    global _ARXIV
    if _ARXIV is None:
        data = json.loads((CATALOG / "arxiv_conjectures.json").read_text())
        by = {}
        for rec in data:
            by.setdefault(rec["arxiv_id"], []).append(rec)
        _ARXIV = {f"{a}__{i:02d}": r for a, recs in by.items() for i, r in enumerate(recs)}
    return _ARXIV.get(cid, {})


def opg_record(slug: str) -> dict:
    global _OPG
    if _OPG is None:
        _OPG = {p["slug"]: p for p in json.loads((CATALOG / "problems.json").read_text())}
    return _OPG.get(slug, {})


def describe(cid: str) -> dict:
    """title, paper, arxiv id, catalog url for an id of either kind."""
    if re.match(r"\d{4}\.\d{4,5}__\d+$", cid):
        r = arxiv_record(cid)
        arxiv = cid.split("__")[0]
        return {
            "title": unlink(r.get("title") or cid),
            "paper": r.get("paper_title") or r.get("paper") or "",
            "arxiv": arxiv,
            "url": f"https://graph-theory-ai.github.io/graph-conjectures/arxiv/{cid}/",
        }
    r = opg_record(cid)
    return {
        "title": r.get("title") or cid,
        "paper": "OpenProblemGarden",
        "arxiv": None,
        "url": f"https://graph-theory-ai.github.io/graph-conjectures/op/{cid}/",
    }


# ---------------------------------------------------------------- building
def pdf_name(cid: str) -> str:
    return f"{cid}__{SLUGS.get(cid, 'result')}__note.pdf"


def referee_fragment(cid: str, outdir: Path) -> Path:
    rheader, rbody = strip_yaml((VERIF / f"{cid}.md").read_text())
    rbody = re.sub(r"(?m)^(?![-*\s]|$)(.+)\n(?=[-*] )", r"\1\n\n", rbody)
    rbody = shift_headings(rbody, 0, drop_first_h1=True)
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

    # The report is intentionally reproduced verbatim, but it is embedded in a
    # different LaTeX document from the source paper and original writeup.  A
    # couple of raw source-label references would therefore render as "??";
    # show their literal label names instead.  Long inline-code paths produced
    # by pandoc are changed from \texttt to \nolinkurl so TeX may break them.
    # The group also keeps dense, machine-generated tables readable without
    # allowing them to spill far into the margin.
    fragment = tex.read_text()
    fragment = fragment.replace(r"\ref{qu:poiluszombius}", r"\texttt{qu:poiluszombius}")
    fragment = fragment.replace(r"\cref{thm:vec-bipartite}", r"\texttt{thm:vec-bipartite}")

    def break_long_code(match):
        body = match.group(1)
        if len(body) < 28 or not ("/" in body or r"\_" in body or "http" in body):
            return match.group(0)
        body = body.replace(r"\_", "_").replace(r"\#", "#").replace(r"\%", "%")
        return r"\nolinkurl{" + body + "}"

    fragment = re.sub(r"\\texttt\{([^{}]*)\}", break_long_code, fragment)
    tex.write_text(
        "\\begingroup\\scriptsize\\sloppy\n"
        "\\setlength{\\tabcolsep}{2pt}\n"
        + fragment
        + "\n\\endgroup\n"
    )
    return tex


def build_note_pdf(cid: str, outdir: Path) -> bool:
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
        print(f"[{cid}] latexmk failed: {errs}", file=sys.stderr)
        return False
    shutil.copy(outdir / ".build" / "note.pdf", HERE / pdf_name(cid))
    return True


def write_index(entries, built):
    rows = []
    order = {"CONFIRMED": 0, "MINOR_GAPS": 1}
    for e in sorted(entries, key=lambda e: (order.get(e["review_verdict"], 9), e["id"])):
        cid = e["id"]
        d = describe(cid)
        paper = f"*{esc(d['paper'])}* ([arXiv:{d['arxiv']}](https://arxiv.org/abs/{d['arxiv']}))" if d["arxiv"] else "OpenProblemGarden"
        name = pdf_name(cid)
        pdf = f"[{name}]({name})" if built.get(cid) else "(note pending)"
        rows.append(f"| [`{cid}`]({d['url']}) | {esc(d['title'])} | {paper} | {LEG_LABEL.get(e.get('leg'), e.get('leg'))} | "
                    f"{e['claimed_verdict']} | [{e['review_verdict']}](../verification_astra/{cid}.md) | {pdf} |")
    n_c = sum(e["review_verdict"] == "CONFIRMED" for e in entries)
    n_m = sum(e["review_verdict"] == "MINOR_GAPS" for e in entries)
    n_built = sum(1 for e in entries if built.get(e["id"]))
    text = f"""# Results to review: gpt-6-astra campaign

The gpt-6-astra campaign (see `../RESULTS_OPG.md`, `../RESULTS_ARXIV_ASTRA.md`,
`../RESULTS_RETRY.md`) produced 31 claims the model itself flagged `would_publish: true`.
All 31 went through the adversarial referee pass in `../verification_astra/`. The
{len(entries)} below survived with verdict **CONFIRMED** ({n_c}) or **MINOR_GAPS** ({n_m},
correct modulo routine repairable details) and were not found to be already in the
literature. The 7 rated ALREADY_KNOWN are excluded here; `../verification_astra/SUMMARY.md`
explains each of those case by case, since one of them (`2402.10782__01`) has a genuinely
new half. Four further survivors that the model labelled `partial` (complete proofs of part
of the posed problem) are held back for a later, separately labelled section.

Each `__note.pdf` is a self-contained mathematical note in the same format as `../to_review/`:
abstract with the AI-provenance disclosure, statement, proof ideas in the main text, full
proofs in Appendix A, the verbatim LLM referee report in Appendix B. Every deviation from the
model's original writeup is declared in the note's Provenance section, and for MINOR_GAPS
items the gaps named by the referee were repaired and marked where they occur.

Sources are in `src/<id>/note.tex`. Regenerate with `python3 to_review_astra/build.py`.
{n_built} of {len(entries)} notes are built.

**Caveat.** Nothing here has been checked by a human mathematician. "CONFIRMED" is the
verdict of an LLM referee, and novelty was checked only against what could be found online.
The margins by which the excluded ALREADY_KNOWN claims lost priority were days to weeks, so
the same could happen to any result below.

| id | problem | source | leg | claim | referee | pdf |
|:--|:--|:--|:--|:--|:--|:--|
""" + "\n".join(rows) + "\n"
    (HERE / "README.md").write_text(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", default=None)
    ap.add_argument("--no-pdf", action="store_true")
    args = ap.parse_args()

    verdicts = json.loads((VERIF / "verdicts.json").read_text())["verdicts"]
    entries = [e for e in verdicts if e["review_verdict"] in KEEP]
    # Results the model itself labelled `partial` (complete proofs of part of the
    # posed problem) are held back for a later, separately labelled section.
    partial = [e for e in entries if e["claimed_verdict"] == "partial"]
    entries = [e for e in entries if e["claimed_verdict"] != "partial"]
    for e in partial:
        for stale in HERE.glob(f"{e['id']}__*.pdf"):
            stale.unlink()
    todo = [e for e in entries if not args.only or e["id"] in args.only]
    built = {}
    for e in todo:
        cid = e["id"]
        outdir = SRC / cid
        outdir.mkdir(parents=True, exist_ok=True)
        if args.no_pdf:
            built[cid] = (HERE / pdf_name(cid)).exists()
            continue
        # superseded outputs for this id (the earlier verbatim-writeup PDFs, old names)
        for stale in HERE.glob(f"{cid}__*.pdf"):
            if stale.name != pdf_name(cid):
                stale.unlink()
        if not (outdir / "note.tex").exists():
            built[cid] = False
            print(f"[{cid}] no note.tex yet")
            continue
        built[cid] = build_note_pdf(cid, outdir)
        print(f"[{cid}] {'ok' if built[cid] else 'FAILED'}")
    for e in entries:
        built.setdefault(e["id"], (HERE / pdf_name(e["id"])).exists())
    write_index(entries, built)


if __name__ == "__main__":
    main()
