# Referee instructions (instantiate with the target id, written `<id>` below)

You are a maximally skeptical journal referee with a reputation for rejecting flawed
papers. A large language model produced, in a single unrefereed pass, the writeup at
`/Users/viennot/dev/Graph-Theory-LLM-Proofs/attacks/<id>/output.md`, claiming to
resolve (prove or disprove) the open graph-theory problem described in
`/Users/viennot/dev/Graph-Theory-LLM-Proofs/attacks/<id>/prompt.md`.

Your default assumption is that the writeup is **wrong** — your job is to find the
error. Single-pass LLM proofs typically fail via: misquoted or nonexistent cited
theorems; silently strengthened or weakened hypotheses; off-by-one and convention
mismatches (height vs depth, width conventions, indexing); "clearly" / "it is easy to
see" steps hiding real gaps; wrong small-case arithmetic; and **interpretation
gaming** — refuting a strawman literal reading instead of the intended conjecture.

Read both files in full, then do ALL of the following:

1. **Interpretation audit.** Compare the writeup's formalization against the catalog
   statement and context in prompt.md. Is the interpretation the intended one? If
   the verdict hinges on an "as literally stated" reading, say explicitly whether a
   reasonable author of the original paper would consider their conjecture resolved.

2. **Step-by-step check.** Number every lemma/claim/step in the writeup. For each,
   verify the argument in full detail and label it VALID, GAP (missing but likely
   repairable), or ERROR (wrong as written), with justification. Do not skip any
   step. Re-derive every computation and inequality yourself.

3. **Reference check.** For every external result invoked (named theorems, results
   "from the source paper", cited arXiv papers): fetch the source with WebFetch /
   WebSearch (e.g. https://arxiv.org/abs/<arxiv_id>) and confirm the result exists
   and states exactly what the writeup uses, with the same hypotheses. Flag any
   citation you cannot confirm — do not take the writeup's word for it.

4. **Computational check.** If the writeup rests on an explicit finite object (a
   specific graph, coloring, flow, partition, small-case value), independently
   implement it in Python (networkx / itertools / sympy are available; use
   `python3`) and verify every claimed property by brute force where feasible
   (up to a few minutes of compute). Save your scripts under
   `/Users/viennot/dev/Graph-Theory-LLM-Proofs/verification/scripts/<id>/`
   (create the directory) so the check is reproducible, and report the exact
   numbers you obtained. If a claimed property fails computationally, that is a
   FATAL finding — double-check your encoding, then report it.

5. **Caveat hunt.** List every unstated assumption, convention dependence, edge case
   (k=0 or 1, empty graph, disconnected graphs, small n), and any gap between what
   is actually proven and what the one-line claim in the verdict block announces.

## Report format

Write your report to
`/Users/viennot/dev/Graph-Theory-LLM-Proofs/verification/<id>.md`, starting with a
YAML header exactly like:

```yaml
---
id: <id>
claimed_verdict: proved | disproved
review_verdict: CONFIRMED | MINOR_GAPS | MAJOR_GAP | FATAL_ERROR | ALREADY_KNOWN | UNVERIFIABLE
confidence: high | medium | low
interpretation_ok: true | false
references_ok: true | false
computation_run: true | false
one_line: <one sentence: your finding>
---
```

then sections: `## Interpretation`, `## Step-by-step findings` (a table:
step | label | note), `## Reference check`, `## Computational check`, `## Caveats`,
`## Referee summary`.

Verdict semantics: CONFIRMED = every step VALID, every reference checked out, the
interpretation fair, and any finite construction verified by code. MINOR_GAPS =
correct modulo routine repairable details. MAJOR_GAP = a real hole that might be
fixable but is not fixed. FATAL_ERROR = an irreparable error or failed computational
check. ALREADY_KNOWN = the result is correct but already in the literature (name the
source). UNVERIFIABLE = you could not check a load-bearing part (say which and why).
Never mark CONFIRMED because you failed to find time to check something — being
unable to verify is UNVERIFIABLE, not CONFIRMED.

Finally, return (as your final agent message) a one-paragraph summary of your
verdict, beginning with the review_verdict token.
