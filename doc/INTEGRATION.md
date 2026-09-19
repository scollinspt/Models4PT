# Models4PT Integration Guide

This guide defines how Models4PT can be developed independently while remaining
usable by the broader clinical inquiry ecosystem. The governing scientific boundaries
remain [Foundational Principles](project-foundation/FOUNDATIONAL_PRINCIPLES.md) and
[System Boundaries](project-foundation/SYSTEM%20BOUNDARIES.md).

## Operating model

Use `Models4PT.code-workspace` for routine implementation, tests, documentation, and
case-study development. Open the clinical-inquiry ecosystem workspace when work crosses
a repository boundary or at the integration checkpoints below. Use the simulation
workspace only when a Models4PT change depends on physiological model development,
solver behavior, or simulation validation.

The repositories remain independently versioned and independently deployable. Do not
couple them through source imports, shared database tables, or assumptions about another
repository's internal classes.

## Knowledge contract

Models4PT owns the contract by which curated population knowledge leaves this system.
Before CIE implementation depends on it, the contract must define:

- stable identifiers for concepts and knowledge objects;
- explicit schema and ontology versions;
- causal structure, mechanisms, populations, contexts, and temporal qualifications;
- measurements and probabilities when available;
- provenance, evidence, assumptions, uncertainty, disagreement, and review state; and
- explicit unresolved or unavailable values rather than silent omission.

The contract should be serializable, documented, and richer than any one diagram or
tool-specific export. Internal dataclasses, persistence models, and API models may
evolve without becoming the cross-project contract.

## Compatibility rules

1. Add a contract fixture representing a small reviewed knowledge package before adding
   a live CIE integration.
2. Validate exported packages against a versioned schema in Models4PT.
3. Keep at least one consumer-oriented test that exercises only the public contract,
   not Models4PT internals.
4. Treat removal, renaming, changed meaning, or tighter validation of a contract field
   as a breaking change unless a migration path preserves compatibility.
5. Record the schema version, ontology version, and Models4PT release or commit in every
   exported package.
6. Keep patient observations, patient identifiers, and patient-specific inference out
   of Models4PT fixtures and APIs.

## Integration checkpoints

Review the change in the clinical-inquiry ecosystem workspace when:

- a milestone changes the meaning or identity of a scientific object;
- a public schema, API, export, or ontology version is introduced or changed;
- a case study reveals a requirement for patient-specific reasoning;
- Models4PT begins consuming a mechanism or evidence representation from another
  project; or
- a Models4PT release is being prepared for use by CIE or another consumer.

At each checkpoint, classify the connection as educational content, a conceptual link,
a shared representation, or a software/data interface. Update the ecosystem coordination
brief when the shared direction, ownership boundary, or active handoff changes.

## Near-term sequence

The current priority remains the narrow provenance-preserving curation workflow in the
README. During that work:

1. Keep persistence and API schemas separate from exploratory domain objects.
2. Exercise new representations against the HF/NMES case study.
3. Capture CIE requirements as contract examples, not patient-reasoning code.
4. Introduce the first versioned export fixture only after reviewed knowledge can be
   persisted and retrieved without losing provenance or curation state.

This sequence lets Models4PT mature on its own terms while making integration an
explicit acceptance criterion rather than a late retrofit.