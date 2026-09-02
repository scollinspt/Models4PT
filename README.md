# Models4PT

Models4PT is an open research platform for building, curating, integrating,
and maintaining computable population-level causal knowledge in physical
therapy and rehabilitation science.

The project asks:

> What do we collectively know?

Models4PT is intended to turn evidence from scientific literature and other
admissible sources into structured knowledge that preserves meaning,
provenance, uncertainty, disagreement, and human review.

## Project boundary

Models4PT constructs and curates population-level scientific knowledge. It is
not a clinical decision-support system and does not perform patient-specific
diagnosis, prognosis, treatment recommendation, or Bayesian inference.

```text
Scientific literature and research knowledge
                    ↓
                 Models4PT
       curated population causal knowledge
                    ↓
        Clinical Inference Engine (CIE)
 population knowledge + individual information
                    ↓
       patient-specific reasoning systems
```

      The Clinical Inference Engine (CIE) is a separate, existing repository whose
      patient-specific reasoning system remains under development. The distinction is
      defined in [System Boundaries](doc/project-foundation/SYSTEM%20BOUNDARIES.md).

      ## Integrated modeling workspace

      Models4PT participates in the shared `~/Projects/physiolog-simulations.code-workspace`
      as the population-level causal knowledge and research-model layer. Physiological
      mechanisms and validation are developed in `hummod-research`; JSim and independent
      solvers execute appropriate equation models; Physiolog derives transparent teaching
      simulations; and CIE consumes appropriate versioned population knowledge for
      patient-specific explanatory and probabilistic reasoning research.

      Workspace membership does not create runtime or source-code coupling. Models4PT and
      CIE remain separate systems connected through explicit, versioned knowledge contracts.

## Scientific principles

Models4PT is governed by several durable commitments:

- The canonical product is curated causal knowledge.
- Concepts, variables, measurements, mechanisms, evidence, and causal claims
  are distinct scientific objects.
- Semantic relationships are distinct from causal relationships.
- AI output is candidate knowledge; researchers remain the scientific authority.
- Accepted knowledge must remain connected to its evidence, assumptions,
  reviewers, and revision history.
- New evidence should refine knowledge without erasing disagreement or
  provenance.

See [Foundational Principles](doc/project-foundation/FOUNDATIONAL_PRINCIPLES.md) for the full statement.

## Current status

Models4PT is in an early research and software-design stage. The repository currently contains a tested Stage 1 domain experiment, not a deployable knowledge platform.

Implemented today:

- Python representations of concepts, variables,measurements, sources,
  evidence, proposed causal claims, and curation decisions
- a deliberately simple candidate-extraction experiment
- an explicit ontology-resolution boundary between extracted terms and
  proposed causal claims
- FastAPI health endpoints
- a minimal React health-check frontend
- backend tests and backend/frontend continuous integration

Not yet implemented:

- persistent storage or a shared ontology repository
- scientific CRUD or query APIs
- publication ingestion
- production AI extraction
- researcher curation screens
- knowledge integration, version history, or governance workflows
- authentication, authorization, or production deployment

The constraints in the current experiment—such as one concept per variable and binary proposed claims—are implementation hypotheses, not final scientific
commitments.

## Repository layout

```text
src/models4pt/              Python package and FastAPI application
tests/                      Backend tests
frontend/                   Vite, React, and TypeScript scaffold
doc/project-foundation/     Governing vision and architecture documents
archive/                    Superseded historical planning material
.github/workflows/          Continuous integration
```

## Development

Python 3.11 is the development and container baseline. Node.js 20.19 is the frontend and CI baseline.

For environment setup, local commands, Docker usage, and validation, see
[Development Guide](doc/DEVELOPMENT.md).

Quick validation after setup:

```bash
python -m pytest -q
npm --prefix frontend run typecheck
npm --prefix frontend run build
```

## Roadmap

The next milestone is a narrow, provenance-preserving curation workflow:

```text
source passage
    ↓
candidate concept and causal claim
    ↓
ontology resolution or explicit unresolved state
    ↓
researcher review with rationale
    ↓
persistent reviewed knowledge record
```

This vertical workflow will establish the repository and curation foundations
before broader literature ingestion, visualization, collaboration, and
downstream reasoning interfaces are attempted.

The longer research and software roadmap is described in the
[Software Project](doc/project-foundation/Models4PT_Software_Project.md) and
[Research Program](doc/project-foundation/Models4PT_Research_Program.md).

## License

Models4PT is released under the [MIT License](LICENSE.txt).

## Contact

Sean M. Collins, PT, ScD — [GitHub](https://github.com/scollinspt)
