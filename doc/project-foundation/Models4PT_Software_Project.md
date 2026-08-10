Models4PT Software Project

Building an Open Platform for Computable Physical Therapy Causal Knowledge

Purpose

The Models4PT software project exists to transform the theoretical goals of the Models4PT research program into a working computational platform.

Models4PT is the research-facing knowledge infrastructure of the broader Clinical Inquiry Platform. Its purpose is to enable researchers to construct, curate, integrate, interrogate, and maintain computable population-level causal knowledge.

The software is not merely an implementation of existing ideas. It is also a research instrument through which new ideas about scientific knowledge representation, causal modeling, ontology development, evidence integration, and computational reasoning can be explored, tested, and refined.

Software development is therefore an integral component of the scientific research process.

Every iteration of the platform should improve both the software itself and the theoretical understanding of how physical therapy knowledge ought to be represented.

Models4PT is governed by the project’s FOUNDATIONAL_PRINCIPLES.md and SYSTEM_BOUNDARIES.md. When implementation choices conflict with those documents, the governing principles and boundaries take precedence unless intentionally revised.

⸻

Development Philosophy

Models4PT will be developed using an iterative, research-driven process.

Rather than attempting to design the complete architecture before implementation, the platform will evolve through repeated cycles of:

* theoretical investigation
* software development
* experimentation
* researcher evaluation
* scientific critique
* refinement

Questions that arise during implementation should drive future research, while new theoretical insights should guide subsequent software development.

Theory and implementation will therefore co-evolve.

Iteration does not mean that foundational distinctions should be repeatedly reinvented. The Foundational Principles and System Boundaries provide stable constraints within which implementation can evolve.

⸻

Software Goals

The platform should enable researchers to:

* construct and curate computable causal knowledge
* extract candidate causal knowledge from scientific publications and other admissible sources
* distinguish concepts, measurements, mechanisms, causal assertions, and evidence
* reconcile new concepts with a shared ontology
* preserve complete provenance
* represent uncertainty and scientific disagreement
* synthesize evidence across publications and other sources
* compare competing hypotheses and mechanisms
* accumulate knowledge through refinement rather than replacement
* assemble question-specific research causal models from the larger repository
* inspect and modify those models
* query accumulated causal knowledge
* visualize causal structures and their supporting evidence
* export appropriate representations for external causal and probabilistic modeling tools
* expose curated knowledge through programmable interfaces
* provide the population-level knowledge infrastructure required by the future Clinical Inference Engine

The software should become an open computational infrastructure for physical therapy causal knowledge.

⸻

Design Principles

Knowledge First

The canonical product of Models4PT is curated causal knowledge.

Scientific publications, datasets, theories, expert contributions, and research models contribute evidence and knowledge to the repository but are not themselves the canonical knowledge representation.

Research models are purposeful views assembled from the larger causal knowledge repository.

Diagrams are representations of those models, not the underlying knowledge itself.

⸻

Distinct Scientific Objects

Concepts, variables, measurements, mechanisms, causal assertions, evidence, populations, contexts, and research models must be represented as distinguishable objects.

The architecture must not require scientifically different things to be represented as though they were equivalent simply because a particular graph or visualization format does so.

The canonical representation should therefore be richer than any individual visualization or export format.

⸻

Explicit Causal Assertions

Causal claims must be represented explicitly and distinguished from statistical associations, semantic relationships, and other forms of scientific relationships.

The system should preserve what kind of claim is being represented, who or what source supports it, and under what assumptions or conditions it applies.

The presence of an association in a publication must not automatically become an accepted causal assertion.

⸻

Ontology-Governed Integration

New concepts must be semantically reconciled with the existing ontology before becoming part of the canonical knowledge repository.

The system should help researchers determine whether a candidate concept:

* corresponds to an existing concept
* is a subtype or specialization
* is a component of another concept
* is a measurement or operationalization of a construct
* is related but scientifically distinct
* represents a genuinely new concept

Ontology alignment should prevent semantic fragmentation without erasing legitimate scientific distinctions.

Semantic relationships and causal relationships must remain distinct.

⸻

Provenance Everywhere

Scientific knowledge must remain traceable.

Causal assertions, mechanisms, measurements, probabilities, evidence, ontology decisions, and other scientifically meaningful objects should retain provenance appropriate to their role.

Where relevant, provenance should include:

* source
* location within the source
* supporting evidence
* contributor
* reviewer
* rationale
* assumptions
* uncertainty or confidence
* competing interpretations
* revision history

Nothing accepted into the repository should become detached from the evidence and decisions that justify its presence.

⸻

Human-AI Collaboration

Large language models and other AI methods should accelerate scientific knowledge extraction, reconciliation, comparison, critique, and model construction.

AI-generated scientific content is candidate knowledge.

Researchers remain responsible for accepting, rejecting, correcting, qualifying, or extending candidate knowledge before it becomes canonical.

The system should support transparent human-AI collaboration rather than autonomous knowledge generation.

⸻

Refinement Rather Than Replacement

The repository should preserve the evolution of scientific understanding.

New evidence may:

* support existing knowledge
* contradict it
* qualify it
* narrow or broaden its applicable context
* identify moderators or boundary conditions
* propose alternative mechanisms
* introduce competing explanations
* change estimates of uncertainty

Scientific disagreement should be represented rather than erased merely to produce a single unified graph.

⸻

Separation of Knowledge Construction and Patient Reasoning

Models4PT constructs and curates population-level causal knowledge.

The Clinical Inference Engine uses appropriate population-level knowledge together with information about an individual patient or case to perform patient-specific causal and probabilistic reasoning.

Models4PT should be designed so that its knowledge can support the CIE, but patient-specific inference does not belong within Models4PT.

⸻

Extensibility

Implementation components should remain replaceable as methods improve.

This includes:

* knowledge extraction methods
* AI models
* ontology services
* storage systems
* graph libraries
* causal analysis libraries
* probabilistic modeling tools
* visualization systems
* search systems
* APIs

Scientific meaning should not depend unnecessarily on a particular implementation technology.

⸻

Development Stages

The stages below describe a proposed development sequence rather than permanent architectural boundaries. They may overlap or be reordered as research and implementation reveal new requirements.

⸻

Stage 1 — Canonical Causal Knowledge Representation

Develop the internal schema required to represent the distinct scientific objects Models4PT must preserve.

Initial objects should include:

* concepts
* variables
* measurements
* mechanisms
* causal assertions
* interventions
* outcomes
* populations
* contexts
* temporal information
* evidence
* publications
* provenance
* uncertainty
* contributor decisions
* reviewer decisions
* version information

The representation must preserve distinctions among ontology relationships, causal relationships, measurements, mechanisms, and evidence.

It should not depend on DAGitty syntax or any other visualization format.

Deliverable

A tested internal library and schema capable of constructing, validating, serializing, and manipulating Models4PT causal knowledge objects.

⸻

Stage 2 — Repository and Ontology Infrastructure

Develop persistent storage for the canonical knowledge representation.

The repository should support:

* concepts and ontology relationships
* causal assertions
* mechanisms
* measurements
* evidence
* publications
* provenance
* uncertainty
* contributor and reviewer decisions
* version history
* research models and model definitions

Research and engineering questions include:

* relational versus graph-oriented storage
* hybrid storage strategies
* ontology representation
* concept identity
* versioning
* provenance modeling
* efficient causal and semantic querying

Deliverable

A persistent, versioned causal knowledge repository with an initial shared ontology.

⸻

Stage 3 — Literature-to-Candidate-Knowledge Pipeline

Develop workflows for converting scientific publications into structured candidate knowledge.

Initial pipeline components include:

1. document import
2. text and metadata extraction
3. identification of candidate concepts and variables
4. identification of measurements
5. identification of candidate causal assertions
6. identification of candidate mechanisms
7. extraction of population and contextual information
8. extraction of relevant evidence and uncertainty
9. ontology reconciliation
10. provenance capture
11. generation of candidate research-model structures
12. researcher review

The output of this pipeline is candidate knowledge, not automatically accepted repository knowledge.

Deliverable

A prototype publication-to-candidate-causal-knowledge workflow with traceable source provenance.

⸻

Stage 4 — Researcher Curation Workflow

Develop the researcher-facing workflow through which candidate knowledge becomes curated knowledge.

Researchers should be able to:

* inspect AI-generated candidate knowledge
* inspect the exact evidence supporting it
* accept or reject candidate assertions
* edit concepts and relationships
* reconcile concepts with the ontology
* distinguish constructs from their measurements
* add missing mechanisms or relationships
* qualify claims by population or context
* record uncertainty
* document rationale
* identify competing interpretations
* connect new knowledge to existing repository knowledge

Deliverable

An interactive human-AI curation workflow capable of transforming candidate knowledge into reviewed repository contributions.

⸻

Stage 5 — Knowledge Integration

Develop methods for integrating newly curated knowledge with the existing repository.

Capabilities should include:

* concept matching
* ontology alignment
* semantic conflict detection
* causal assertion comparison
* evidence aggregation
* supporting-evidence identification
* contradictory-evidence identification
* contextual qualification
* competing hypothesis representation
* mechanism comparison
* uncertainty representation
* provenance-preserving integration

Integration should not simply collapse similar knowledge into a single assertion.

Deliverable

A provenance-preserving workflow for accumulating causal knowledge across multiple publications and contributors.

⸻

Stage 6 — Research Model Assembly and Analysis

Develop tools for assembling question-specific research models from the larger repository.

A researcher should be able to begin with a research question and obtain a candidate model containing relevant:

* exposures
* outcomes
* confounders
* mediators
* moderators
* colliders
* selection mechanisms
* causal mechanisms
* contextual variables
* competing structures
* supporting evidence

Researchers should be able to expand, reduce, modify, critique, and save these models.

The platform should support translation of appropriate research models into formats suitable for:

* Directed Acyclic Graphs
* DAGitty
* Structural Causal Models
* Bayesian Networks
* Probabilistic Graphical Models
* Python and R analysis workflows

These are representations or analytical projections of repository knowledge rather than the canonical storage format.

Deliverable

A research-question-to-editable-causal-model workflow backed by the repository.

⸻

Stage 7 — Knowledge API

Expose curated population causal knowledge through stable programmable interfaces.

Capabilities should eventually include:

* concept retrieval
* ontology browsing
* causal knowledge queries
* mechanism queries
* evidence lookup
* provenance inspection
* population and context filtering
* research model retrieval
* model assembly requests
* version comparison
* knowledge-history inspection
* export into supported modeling formats

The API should expose scientific meaning without requiring downstream systems to depend on Models4PT’s internal storage implementation.

The interface should eventually support the Clinical Inference Engine in requesting the subset of population-level knowledge relevant to a particular reasoning problem.

Deliverable

A documented programmatic interface to curated Models4PT knowledge.

⸻

Stage 8 — Visualization and Scientific Exploration

Develop interactive interfaces for exploring:

* causal knowledge
* question-specific research models
* ontology relationships
* mechanisms
* supporting evidence
* conflicting evidence
* uncertainty
* provenance
* competing hypotheses
* model alternatives

Visualization should function as an exploratory and scientific review tool rather than merely a graphical display.

Users should be able to move readily between a visual relationship and the evidence, assumptions, and provenance underlying it.

Deliverable

An interactive research environment for visual exploration and critique of repository knowledge.

⸻

Stage 9 — Collaboration and Governance

Support distributed scientific development through:

* contributor attribution
* researcher review
* knowledge proposals
* change history
* ontology review
* causal assertion review
* model comparison
* evidence auditing
* conflict resolution
* version control
* repository governance

Scientific knowledge should be able to evolve collaboratively while retaining accountability for who proposed, reviewed, changed, and accepted each contribution.

Deliverable

A collaborative governance workflow for an open causal knowledge repository.

⸻

Technology Strategy

Technology choices should follow the scientific representation rather than determine it.

Initial candidates include:

Backend

* Python
* FastAPI or equivalent API framework

Storage

* PostgreSQL
* graph-oriented representations or extensions where useful
* vector or semantic indexes where useful

Scientific Computing

* NetworkX
* pgmpy
* NumPy
* SciPy
* additional causal inference libraries as appropriate

Artificial Intelligence

* LLM-assisted candidate knowledge extraction
* structured-output generation
* embedding-based semantic retrieval
* ontology alignment assistance
* scientific literature comparison
* AI-assisted model critique

Frontend

* modern web application framework
* interactive causal graph visualization
* ontology browser
* evidence and provenance interfaces
* researcher curation tools

Infrastructure

* GitHub
* automated testing
* continuous integration
* reproducible environments
* containerized deployment where appropriate

These are implementation hypotheses rather than permanent commitments.

The scientific schema, provenance model, and interface contracts should remain as independent as practical from particular technologies.

⸻

Research Through Software

Implementation should continually expose unanswered scientific and computational questions.

Examples include:

* What constitutes the identity of a causal concept?
* What constitutes the identity of a causal variable?
* When should two concepts be considered equivalent?
* When should they remain distinct?
* How should constructs and their measurements be related?
* How should causal mechanisms be represented?
* How should causal assertions be qualified by population and context?
* How should conflicting evidence be represented?
* How should uncertainty be represented without implying false precision?
* How should knowledge change through time?
* What constitutes sufficient evidence for accepting a candidate causal assertion?
* How should competing causal explanations coexist?
* What is the smallest useful question-specific causal model?
* How should large causal knowledge structures be decomposed and recomposed?
* Can hierarchical causal representations adequately capture biological, behavioral, social, and environmental organization?
* What information must population-level knowledge preserve so that the Clinical Inference Engine can later perform defensible patient-specific reasoning?

Architectural decisions should be used to refine the underlying scientific theory, while remaining constrained by the Foundational Principles and System Boundaries.

⸻

Success Criteria

The Models4PT software project will have reached an important initial level of success when it can:

* import a published physical therapy study
* extract a traceable set of AI-generated candidate concepts, measurements, mechanisms, and causal assertions
* allow a researcher to review and correct those candidates
* reconcile concepts with the existing ontology
* preserve evidence and provenance for accepted knowledge
* add reviewed knowledge to a persistent repository
* integrate additional studies without erasing disagreement or provenance
* assemble repository knowledge into a question-specific causal research model
* allow researchers to inspect and revise that model
* expose the underlying knowledge through an open programmatic interface
* export appropriate representations to external causal and probabilistic modeling tools
* provide a robust population-level knowledge layer capable of supporting the future Clinical Inference Engine

A later measure of success will be whether independent researchers can contribute to and reuse the repository while preserving scientific transparency, interoperability, and conceptual coherence.

⸻

Long-Term Vision

Models4PT is intended to become more than a causal modeling application.

It is envisioned as an open scientific infrastructure for representing, integrating, interrogating, and evolving computable physical therapy causal knowledge.

Researchers will contribute not merely diagrams or isolated publications, but reviewed scientific knowledge connected to evidence, ontology, provenance, uncertainty, and competing explanations.

Research models will be assembled from that shared knowledge for particular scientific questions rather than becoming isolated knowledge silos.

As the repository grows, Models4PT should support a continuously improving computational representation of the discipline’s population-level causal understanding.

That knowledge infrastructure will remain distinct from, while being intentionally designed to support, the Clinical Inference Engine and future research, educational, and clinical applications within the broader Clinical Inquiry Platform.