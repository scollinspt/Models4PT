The HF/NMES model as it is reviewed and refined through the Models4PT
workflow — concepts, variables, measurements, causal claims, evidence, and
curation decisions (using the Stage 1 domain objects in `src/models4pt` where
applicable).

Starting point: `Model4b.docx` — DAGitty code for model 4D, the most complete
draft (pictured as `Model4.png` in `../synthesis/`). Other files here
(`Model1.docx`, `Model2.docx`, `Model2a.docx`, `Model3.docx`) are earlier
draft iterations, kept for history/traceability.

- `model4d_dagitty.txt` — model 4D's DAGitty code, transcribed cleanly from
  `Model4b.docx` for reference.
- `model_4d.py` — translates model 4D's 17 variables and 27 edges into
  Stage 1 domain objects (`Concept`/`Variable`/`ProposedCausalClaim`) from
  `src/models4pt/domain.py`. Run directly (`python model_4d.py`) to print a
  summary. Every claim currently has an empty `evidence` list, since DAGitty
  carries no per-edge evidence — the first concrete gap this case study
  surfaces; see `../notes.md`.
- `mechanisms.py` — first worked example of the instantiation-representation
  problem (see `../notes.md`): a `ProposedMechanism` type describing a
  candidate causal pathway to a shared effect plus the literature-based
  measurements that could differentiate it from competing pathways to the
  same effect, still entirely at the population level (no patient
  classification — that's the CIE's job, out of scope here). Four draft
  mechanisms converging on `six_mwd` (peripheral, cardiac, balance/gait,
  mechanical-efficiency), pending author review. Run directly
  (`python mechanisms.py`) to print a summary.

DAGitty only captures possible causal connections (variables + directed
edges), not the evidence/provenance/measurement structure Models4PT needs, so
expect refined content here to diverge from the DAGitty source as curation
proceeds.
