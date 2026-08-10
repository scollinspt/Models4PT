# Models4PT

**Models4PT is an open research platform for building, curating, integrating, and maintaining computable population-level causal knowledge in physical therapy.**

Models4PT is part of the broader **Clinical Inquiry Platform**. Its purpose is to help researchers transform scientific literature and other admissible knowledge sources into a curated, provenance-preserving representation of what is collectively known about causal structure, mechanisms, context, uncertainty, and evidence.

Models4PT is designed to answer a population-level question:

> **What do we collectively know?**

It provides knowledge infrastructure that can support downstream reasoning systems, including a future **Clinical Inference Engine**, which addresses a different question:

> **Given this patient, what does that knowledge imply?**

Models4PT is **not** itself a clinical decision support system and does not perform patient-specific diagnosis, prognosis, treatment recommendation, or Bayesian inference.

---

## Vision

Scientific knowledge should accumulate as structured, computable knowledge rather than remain fragmented across disconnected publications, datasets, diagrams, and narrative summaries.

In Models4PT, research contributes to an evolving scientific knowledge repository in which distinct scientific objects can be represented explicitly and connected to their supporting evidence.

These objects may include:

- concepts
- variables
- measurements
- mechanisms
- causal assertions
- interventions
- outcomes
- populations
- contexts
- temporal relationships
- uncertainty
- evidence
- provenance
- competing hypotheses
- contributor and reviewer decisions
- version history

The long-term goal is an open scientific infrastructure through which physical therapy causal knowledge can be constructed, examined, challenged, refined, reused, and exposed computationally.

---

## Core Principle: Knowledge First

The canonical product of Models4PT is the **curated causal knowledge repository**.

Scientific publications, datasets, theories, expert contributions, and research models may contribute evidence and knowledge to the repository, but they are not themselves the canonical knowledge representation.

Likewise, diagrams are representations of knowledge rather than the knowledge itself.

The internal representation must therefore be richer than any individual graph, visualization, or export format.

---

## Project Architecture

```text
Scientific Literature and Other Knowledge Sources
                        │
                        ▼
          AI-Assisted Candidate Extraction
                        │
                        ▼
               Candidate Knowledge
                        │
            ┌───────────┴───────────┐
            ▼                       ▼
   Ontology Reconciliation   Researcher Review
            │                       │
            └───────────┬───────────┘
                        ▼
             Curated Causal Knowledge
                        │
                        ▼
              Models4PT Repository
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
    Research Models   APIs     Scientific Exploration
          │
          ▼
 DAGs / SCMs / Bayesian Networks /
 other analytical representations

                        │
                        ▼
            Clinical Inference Engine
     population knowledge + patient information
                        │
                        ▼
             Patient-specific reasoning
```

Models4PT constructs and curates **population-level scientific knowledge**.

The Clinical Inference Engine is a separate system responsible for instantiating appropriate population knowledge for an individual patient or case and performing patient-specific causal and probabilistic reasoning.

---

## Distinct Scientific Objects

Models4PT intentionally distinguishes scientific objects that are often collapsed together in simpler graph-based systems.

For example:

- a **concept** is not the same thing as a measurement of that concept
- a **measurement** is not the same thing as the underlying construct
- a **causal assertion** is not the same thing as a statistical association
- a **mechanism** is not merely an edge in a diagram
- an **ontology relationship** is not a causal relationship
- a **research model** is not the canonical repository itself

Preserving these distinctions is necessary for scientifically coherent knowledge integration.

## Stage 1 Domain Experiment Baseline

The current backend domain implementation is accepted as the first Models4PT Stage 1 domain experiment baseline.
It is intentionally minimal and experimental; the following constraints are not final scientific commitments:

- one Concept per Variable
- binary `ProposedCausalClaim`
- cause and effect must have different `variable_id` values
- no `Observation`/`MeasurementResult` object yet
- no `CanonicalCausalAssertion` yet
- no DAG or global acyclicity constraint

---

## Minimal Backend Scaffold

This repository now includes a minimal Python backend scaffold for Models4PT using FastAPI.

### Start the app

```bash
python -m uvicorn src.models4pt.app:app --reload
```

### Run tests

```bash
python -m pip install -e .[test]
python -m pytest
```

### What’s included

- `pyproject.toml` for Python packaging and dependencies
- `src/models4pt/app.py` FastAPI application with basic health endpoints
- `tests/test_app.py` minimal HTTP tests using FastAPI TestClient
- GitHub Actions workflow at `.github/workflows/python-app.yml`

Existing project foundation documents remain in `doc/project-foundation/`.

---

## Shared Ontology

Models4PT includes a shared ontology that provides the semantic structure required to integrate knowledge contributed across studies and researchers.

The ontology supports:

- concept identity
- preferred terminology and synonyms
- broader and narrower concepts
- subtypes
- components
- related concepts
- anatomical and physiological entities
- impairments
- movement-related constructs
- interventions
- outcomes
- environmental and contextual factors
- measurements and their relationships to constructs

When new candidate concepts are introduced, the system should help determine whether they:

- correspond to an existing concept
- represent a subtype or specialization
- are a component of another concept
- are a measurement or operationalization of a construct
- are related but scientifically distinct
- represent a genuinely new concept

**Semantic relationships and causal relationships remain distinct.**

The ontology establishes what scientific objects mean and how they relate conceptually. It does not determine that one entity causes another.

---

## Causal Knowledge Repository

The causal knowledge repository is the canonical scientific product maintained by Models4PT.

It is not simply a database of publications or a collection of independent causal diagrams.

The repository should preserve:

- causal structure
- mechanisms
- measurements
- applicable populations and contexts
- temporal information
- evidence
- assumptions
- uncertainty
- provenance
- supporting evidence
- conflicting evidence
- qualifying evidence
- competing explanations
- contributor decisions
- reviewer decisions
- ontology versions
- knowledge versions

Every accepted causal assertion should remain connected to the evidence, assumptions, and human decisions supporting its presence in the repository.

---

## Refinement Rather Than Replacement

Scientific knowledge does not evolve only by replacing an old claim with a new one.

New evidence may:

- support existing knowledge
- contradict it
- qualify it
- narrow or broaden its applicable context
- identify moderators or boundary conditions
- propose alternative mechanisms
- introduce competing explanations
- alter uncertainty
- motivate revision of previously accepted knowledge

Models4PT is intended to preserve this scientific evolution.

Disagreement should be represented rather than erased merely to produce a single consensus graph.

---

## Human-AI Collaboration

AI is a capability within Models4PT, not the scientific authority.

Large language models and other AI methods may assist with:

- literature interpretation
- candidate concept identification
- candidate variable extraction
- measurement extraction
- candidate causal assertion extraction
- mechanism extraction
- population and context extraction
- ontology alignment
- evidence comparison
- identification of related existing knowledge
- candidate model construction
- scientific critique

AI-generated scientific content remains **candidate knowledge** until appropriately reviewed.

Researchers remain responsible for accepting, rejecting, correcting, qualifying, or extending candidate knowledge before it becomes canonical.

---

## Literature-to-Knowledge Workflow

A planned literature-to-knowledge workflow includes:

1. document import
2. text and metadata extraction
3. candidate concept and variable identification
4. measurement identification
5. candidate causal assertion extraction
6. mechanism extraction
7. population and contextual extraction
8. evidence and uncertainty extraction
9. ontology reconciliation
10. provenance capture
11. candidate research-model generation
12. researcher review
13. integration into the curated repository

The output of automated extraction is not automatically accepted scientific knowledge.

---

## Research Models

A **research model** is a purposeful representation assembled from the larger causal knowledge repository for a particular:

- research question
- explanatory problem
- study-design problem
- evidence-synthesis task
- hypothesis
- educational purpose

A research model is a **view of the repository**, not the repository itself.

Research models may expose relevant:

- exposures
- interventions
- outcomes
- confounders
- mediators
- moderators
- colliders
- selection processes
- mechanisms
- contextual variables
- uncertainty
- supporting evidence
- competing structures or hypotheses

Researchers should be able to inspect, expand, reduce, modify, critique, and save these models.

Reviewed refinements may subsequently be proposed back to the canonical repository through the Models4PT curation process.

---

## Graphical and Analytical Representations

Models4PT may translate appropriate research models into formats suitable for:

- Directed Acyclic Graphs (DAGs)
- DAGitty
- Structural Causal Models
- Bayesian Networks
- Probabilistic Graphical Models
- Python and R analytical workflows

These are **representations or analytical projections** of repository knowledge.

No single graph format defines the canonical Models4PT knowledge representation.

---

## Provenance Everywhere

Scientific knowledge must remain traceable.

Where appropriate, Models4PT should preserve provenance including:

- source
- location within the source
- supporting evidence
- contributor
- reviewer
- rationale
- assumptions
- uncertainty or confidence
- competing interpretations
- revision history

Knowledge should not become detached from the evidence and decisions that justify its inclusion.

---

## Knowledge Integration

Models4PT is intended to integrate knowledge across publications and contributors without collapsing meaningful differences.

Knowledge integration may require:

- concept matching
- ontology alignment
- semantic conflict detection
- causal assertion comparison
- evidence aggregation
- supporting-evidence identification
- contradictory-evidence identification
- contextual qualification
- mechanism comparison
- competing-hypothesis representation
- uncertainty representation
- provenance-preserving integration

Integration is therefore not equivalent to merging similar edges into a single graph.

---

## Researcher Curation

Researchers are central to the Models4PT workflow.

The platform should allow researchers to:

- inspect AI-generated candidate knowledge
- inspect the exact evidence supporting a candidate
- accept or reject candidate assertions
- correct concepts and relationships
- reconcile concepts with the shared ontology
- distinguish constructs from their measurements
- add missing mechanisms or relationships
- qualify claims by population or context
- record uncertainty
- document rationale
- identify competing interpretations
- connect new knowledge to existing repository knowledge

This human review process is what transforms candidate knowledge into curated scientific knowledge.

---

## Relationship to the Clinical Inference Engine

Models4PT and the Clinical Inference Engine serve complementary but separate purposes.

| Models4PT | Clinical Inference Engine |
|---|---|
| Population-level scientific knowledge | Individual patient or case reasoning |
| Knowledge construction and curation | Knowledge application |
| Literature and research evidence | Patient observations and history |
| Canonical ontology | Uses ontology information |
| Canonical causal knowledge repository | Patient-specific model instantiation |
| Scientific uncertainty | Patient-level uncertainty propagation |
| Research models | Patient-specific explanatory and probabilistic models |
| `"What do we collectively know?"` | `"What does this imply for this patient?"` |

The primary boundary is:

```text
Models4PT:
Scientific literature and research knowledge
        ↓
Curated population causal knowledge


Clinical Inference Engine:
Population causal knowledge + individual patient information
        ↓
Patient-specific causal and probabilistic reasoning
```

Patient-specific inference must not silently modify canonical population knowledge.

Knowledge generated through patient-level use may eventually motivate scientific research or repository revision, but such changes must enter Models4PT through its scientific curation and provenance process.

---

## API

Models4PT is intended to expose curated population-level knowledge through stable programmable interfaces.

Future API capabilities may include:

- concept retrieval
- ontology browsing
- causal knowledge queries
- mechanism queries
- evidence lookup
- provenance inspection
- population and context filtering
- research model retrieval
- model assembly requests
- version comparison
- knowledge-history inspection
- export into supported modeling formats

The API should expose scientific meaning without requiring downstream systems to depend on Models4PT's internal storage implementation.

It should eventually allow the Clinical Inference Engine to request only the portions of population knowledge relevant to a particular reasoning problem.

---

## Scientific Exploration and Visualization

Models4PT is intended to support interactive exploration of:

- causal knowledge
- research models
- ontology relationships
- mechanisms
- supporting and conflicting evidence
- uncertainty
- provenance
- competing hypotheses
- model alternatives

Visualization is intended to function as a scientific exploration and review tool, not merely as graphical display.

Users should be able to move from a visual relationship to the evidence, assumptions, context, uncertainty, and provenance underlying it.

---

## Collaboration and Governance

Long-term collaborative capabilities may include:

- contributor attribution
- researcher review
- knowledge proposals
- change history
- ontology review
- causal assertion review
- model comparison
- evidence auditing
- conflict resolution
- version control
- repository governance

The aim is collaborative scientific knowledge development with accountability for who proposed, reviewed, changed, and accepted each contribution.

---

## Initial Application Domain

Initial development focuses on **physical therapy and rehabilitation research**.

The project is intended to create an open computational infrastructure for physical therapy causal knowledge while preserving implementation flexibility and scientific extensibility as the research program develops.

---

## Development Roadmap

The current proposed development sequence is:

1. **Canonical causal knowledge representation**  
   Define and test the internal scientific schema.

2. **Repository and ontology infrastructure**  
   Build persistent, versioned storage and an initial shared ontology.

3. **Literature-to-candidate-knowledge pipeline**  
   Convert publications into structured, traceable candidate knowledge.

4. **Researcher curation workflow**  
   Enable human review and transformation of candidates into curated contributions.

5. **Knowledge integration**  
   Accumulate evidence across studies while preserving provenance, context, disagreement, and uncertainty.

6. **Research model assembly and analysis**  
   Assemble question-specific models from repository knowledge.

7. **Knowledge API**  
   Expose curated knowledge through stable programmatic interfaces.

8. **Visualization and scientific exploration**  
   Build interactive tools for examining causal knowledge and its evidentiary basis.

9. **Collaboration and governance**  
   Support distributed scientific contribution, review, auditing, and versioned change.

These stages are a proposed development sequence rather than permanent architectural boundaries and may overlap as implementation and research evolve.

---

## Technology Strategy

Technology choices should follow the scientific representation rather than determine it.

Current implementation candidates include:

### Backend

- Python
- FastAPI or an equivalent API framework

### Storage

- PostgreSQL
- graph-oriented representations or extensions where useful
- vector or semantic indexes where useful

### Scientific Computing

- NetworkX
- pgmpy
- NumPy
- SciPy
- additional causal-inference libraries as appropriate

### Artificial Intelligence

- LLM-assisted candidate knowledge extraction
- structured-output generation
- embedding-based semantic retrieval
- ontology alignment assistance
- scientific literature comparison
- AI-assisted model critique

### Frontend

- modern web application framework
- interactive causal graph visualization
- ontology browser
- evidence and provenance interfaces
- researcher curation tools

### Infrastructure

- GitHub
- automated testing
- continuous integration
- reproducible environments
- containerized deployment where appropriate

These are **implementation hypotheses, not permanent commitments**.

The scientific schema, provenance model, and interface contracts should remain as independent as practical from any particular technology.

---

## Research Through Software

Models4PT is both software infrastructure and a research instrument.

Implementation is expected to expose unresolved scientific and computational questions, including:

- What constitutes the identity of a causal concept?
- What constitutes the identity of a causal variable?
- When should two concepts be considered equivalent?
- When should they remain distinct?
- How should constructs and measurements be related?
- How should mechanisms be represented?
- How should causal assertions be qualified by population and context?
- How should conflicting evidence be represented?
- How should uncertainty be represented without implying false precision?
- How should scientific knowledge change through time?
- What constitutes sufficient evidence for accepting a candidate causal assertion?
- How should competing causal explanations coexist?
- How should large causal knowledge structures be decomposed and recomposed?
- Can hierarchical causal representations adequately capture biological, behavioral, social, and environmental organization?
- What population-level information must be preserved to support defensible patient-specific reasoning?

Theory and implementation are expected to co-evolve, while foundational principles and system boundaries provide stable constraints on architectural development.

---

## Current Prototype

The repository currently contains early prototypes from the project's earlier causal-modeling work.

Clone the repository:

```bash
git clone https://github.com/scollinspt/Models4PT.git
```

The legacy browser-based prototype can be opened from:

```text
gui/dags.html
```

The current prototype should be understood as an experimental predecessor to the broader knowledge infrastructure described in this README.

---

## Origins

Models4PT was originally inspired by **DAGitty** and the work of **Johannes Textor**, whose contributions demonstrated the value of graphical causal models for scientific reasoning and causal inference.

Early prototypes explored extending DAGitty-style causal modeling for rehabilitation research.

As the research program evolved, Models4PT expanded beyond an interactive DAG editor toward a broader scientific infrastructure for:

- causal knowledge representation
- shared ontology development
- AI-assisted candidate knowledge extraction
- researcher curation
- evidence integration
- provenance
- uncertainty
- versioned scientific knowledge
- research-model assembly
- machine-readable population knowledge

The DAGitty project remains an important intellectual influence on the development of Models4PT.

---

## Theoretical Foundations

Models4PT is grounded in work spanning causal inference, probabilistic graphical modeling, philosophy of science, biomedical knowledge representation, and the relationship between population knowledge and patient-specific reasoning.

Its architecture is informed by complementary perspectives including:

- Structural Causal Models and Directed Acyclic Graphs
- Bayesian reasoning and probabilistic graphical models
- scientific model synthesis and knowledge integration
- mechanistic explanation
- critical realism
- ontology and semantic knowledge representation
- provenance and scientific uncertainty
- the transition from population-level knowledge to patient-specific clinical reasoning

Selected publications motivating the project include:

- **Collins, S.M. (2026). _From Population Knowledge to Patient Reasoning._**  
  https://philpapers.org/rec/COLFPK

- **Collins, S.M. (2018). _Synthesis: Causal Models, Causal Knowledge, and Scientific Representation._**  
  *Cardiopulmonary Physical Therapy Journal.*  
  https://doi.org/10.1097/CPT.0000000000000101

---

## Project Boundaries

Models4PT is one layer within the broader Clinical Inquiry Platform:

```text
Clinical Inquiry
scientific and philosophical foundations
        ↓
Models4PT
computable population causal knowledge
        ↓
Clinical Inference Engine
patient-specific causal and probabilistic reasoning
        ↓
Applications
research, educational, clinical, and other workflows
```

The systems are intended to remain interoperable but conceptually distinct.

Models4PT owns construction and curation of population scientific knowledge.

The Clinical Inference Engine owns patient-specific reasoning.

Applications provide user-facing workflows.

Clinical Inquiry provides the theoretical and philosophical foundation.

---

## Project Status

Models4PT is an evolving open-source research project.

The present repository contains early software prototypes while the canonical scientific representation, repository architecture, ontology, curation workflows, and knowledge-integration infrastructure are being developed.

The architecture is expected to evolve through repeated cycles of theoretical investigation, implementation, experimentation, researcher evaluation, scientific critique, and refinement.

---

## Contact

**Sean M. Collins, PT, ScD**

GitHub: https://github.com/scollinspt

---

*Models4PT is an open research project exploring how population-level causal knowledge in physical therapy can be represented, curated, integrated, interrogated, and made computationally reusable.*
