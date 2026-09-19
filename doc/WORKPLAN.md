# Models4PT Active Workplan

This document is the repository-wide operational workplan. It tracks the current
milestone, immediate decisions, implementation sequence, and completion criteria.
Long-range scientific and architectural direction remains in
[project-foundation](project-foundation/), while case-study-specific work remains
in each case study's notes.

## Current milestone

Build a narrow, provenance-preserving curation workflow:

```text
source passage
    -> candidate concept and causal claim
    -> ontology resolution or explicit unresolved state
    -> researcher review with rationale
    -> persistent reviewed knowledge record
```

The first step is to define the minimal reviewed knowledge record and the rules
that govern its creation. Open design questions are in
[CURATION_RECORD_QUESTIONS.md](CURATION_RECORD_QUESTIONS.md).

## Working definitions

### Fields

Fields are the information stored in a record. The initial working set is:

- a stable record identifier;
- the source passage and its publication or source reference;
- the candidate concept or proposed causal claim being reviewed;
- the ontology resolution for each referenced concept, including an explicit
  unresolved state;
- the researcher's decision, such as accept, reject, revise, or defer;
- the reviewer's identity;
- the rationale for the decision;
- creation and decision timestamps; and
- version or revision information.

These fields are proposals, not a final persistence schema. The current domain
objects remain exploratory and should not automatically become database or API
models.

### Invariants

Invariants are rules the software must always enforce. The initial working rules
are:

1. AI-generated output remains candidate knowledge until a human records an
   explicit curation decision.
2. Accepted knowledge remains linked to its source, evidence, and provenance.
3. A causal claim with unresolved concepts cannot become accepted knowledge.
4. Every curation decision identifies its human reviewer.
5. Decisions requiring justification retain the reviewer's rationale.
6. Revisions preserve prior records and decisions rather than overwriting their
   history.
7. Rejection or deferral does not erase the candidate or its provenance.

## Planned sequence

1. Answer and review the curation-record questions.
2. Convert the answers into an agreed record specification and acceptance
   criteria.
3. Add the smallest behavior-level tests for the agreed invariants.
4. Implement an in-memory curation workflow through a dedicated application or
   domain boundary.
5. Exercise the workflow with one focused HF/NMES example.
6. Choose and implement persistence only after the record semantics work in
   memory.
7. Add retrieval tests proving that provenance and curation state survive a
   round trip.

## Milestone completion criteria

The milestone is complete when one source passage can move through candidate
extraction, ontology resolution, explicit human review, persistence, and
retrieval without losing:

- the original source and passage;
- unresolved or resolved concept state;
- the proposed claim;
- the reviewer, decision, and rationale; or
- revision history.

No AI-generated candidate may be treated as accepted repository knowledge
without an explicit human decision.

## Worklog

### 2026-09-19

- Established this repository-wide active workplan.
- Identified the minimal reviewed knowledge record as the next design step.
- Recorded working field and invariant definitions.
- Created a question worksheet for the principal investigator before schema or
  persistence implementation begins.
