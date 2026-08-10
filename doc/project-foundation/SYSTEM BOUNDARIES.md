SYSTEM BOUNDARIES

Purpose

This document defines the major conceptual and functional boundaries within the Clinical Inquiry Platform ecosystem.

Its purpose is to prevent architectural drift, duplication of responsibility, and inappropriate coupling as Models4PT, the Clinical Inference Engine, and downstream applications evolve.

These boundaries are subordinate to the Models4PT Foundational Principles. Implementation details may change. These responsibilities should change only through an explicit architectural decision.

⸻

1. Clinical Inquiry

Role

Clinical Inquiry provides the philosophical and theoretical foundation for the ecosystem.

It addresses questions concerning the nature of scientific and clinical knowledge, causal explanation, uncertainty, and the translation of population-level knowledge into reasoning about individual patients.

Clinical Inquiry Owns

* the philosophical framework for clinical reasoning
* the theoretical relationship between population knowledge and patient-specific reasoning
* the conceptual foundations of causal and explanatory modeling
* the epistemological framework governing knowledge, evidence, uncertainty, and inference
* scholarly development of these ideas through research and publication

Clinical Inquiry Does Not Own

Clinical Inquiry is not the deployed knowledge repository, causal modeling application, inference engine, or clinical application.

It provides the scientific foundation from which those systems are developed.

⸻

2. Models4PT

Role

Models4PT is the research-facing computational knowledge infrastructure for building, curating, integrating, and maintaining population-level causal knowledge.

Its primary users are researchers and scientific knowledge contributors.

Its canonical product is the curated causal knowledge repository.

Models4PT Owns

Models4PT is responsible for:

* importing scientific literature and other admissible knowledge sources
* AI-assisted extraction of candidate concepts, variables, mechanisms, causal assertions, measurements, interventions, outcomes, and other scientific objects
* researcher review, correction, acceptance, rejection, and refinement of AI-generated candidate knowledge
* construction and refinement of research causal models
* semantic reconciliation of new concepts with the existing ontology
* ontology development and maintenance
* representation of population-level causal knowledge
* representation of mechanisms and causal structure
* representation of uncertainty associated with scientific knowledge
* evidence integration across publications and other sources
* explicit representation of supporting, conflicting, qualifying, and competing evidence
* provenance
* contributor and reviewer attribution
* version history
* collaborative scientific knowledge development
* model assembly for research questions
* visualization and interrogation of population-level causal knowledge
* export to appropriate causal and probabilistic modeling formats
* APIs through which other systems can retrieve curated knowledge

Models4PT Does Not Own

Models4PT does not own:

* individual patient records
* patient-specific causal model instantiation
* patient-specific Bayesian or probabilistic inference
* diagnosis of an individual patient
* treatment recommendations for an individual patient
* patient-specific prognosis
* clinical decision-making workflows
* end-user clinical applications

Models4PT may support research into these problems and may provide research tools for testing its knowledge structures, but patient-specific reasoning belongs to the Clinical Inference Engine.

⸻

3. The Shared Ontology

Role

The ontology provides the shared semantic structure required for independently developed causal knowledge to be integrated coherently.

It establishes what scientific objects mean and how they relate conceptually.

The ontology is part of the Models4PT knowledge infrastructure, but it must remain logically distinguishable from the causal knowledge stored using it.

The Ontology Owns

The ontology represents concepts and semantic relationships such as:

* concept identity
* synonyms and preferred terminology
* broader and narrower concepts
* subtypes
* components
* related concepts
* anatomical entities
* physiological entities and systems
* impairments
* movement-related constructs
* interventions
* outcomes
* environmental factors
* patient goals
* measurements and their relationships to constructs

The ontology supports determination of whether a newly proposed concept:

* corresponds to an existing concept
* is a subtype or specialization of an existing concept
* is a component of another concept
* is a measurement or operationalization of a concept
* is related but scientifically distinct
* represents a genuinely new concept

The Ontology Does Not Own

The ontology does not determine that one scientific entity causes another.

Semantic relationships and causal relationships must remain distinct.

For example, identifying two terms as referring to the same construct is an ontology operation. Determining that the construct causally affects an outcome is a causal knowledge operation.

⸻

4. The Causal Knowledge Repository

Role

The causal knowledge repository is the canonical scientific product maintained by Models4PT.

It represents accumulated population-level scientific knowledge in a form that can be inspected by humans and consumed computationally.

The repository is not simply a collection of publications or a collection of independent diagrams.

The Repository Contains

The repository may contain distinct but connected scientific objects including:

* concepts
* variables
* measurements
* mechanisms
* causal assertions
* interventions
* outcomes
* contextual conditions
* populations
* temporal relationships
* uncertainty
* evidence
* publications
* provenance
* competing hypotheses
* contributor decisions
* reviewer decisions
* version history
* research models

Every causal assertion must remain connected to the evidence, assumptions, and human decisions supporting its presence in the repository.

Repository Evolution

New evidence does not automatically replace existing knowledge.

It may:

* support existing knowledge
* contradict it
* qualify it
* narrow or broaden its applicable context
* identify moderators or boundary conditions
* propose alternative mechanisms
* introduce competing explanations
* change uncertainty
* motivate revision of previously accepted knowledge

Scientific disagreement should be represented rather than erased merely to produce a single consensus graph.

⸻

5. Research Models

Role

A research model is a purposeful representation assembled from the larger causal knowledge repository for a particular research question, explanatory problem, study design, evidence synthesis task, or educational purpose.

A research model is a view of the repository, not the repository itself.

Research Models May

* select a relevant subset of repository knowledge
* organize knowledge around an exposure, intervention, outcome, or research question
* expose relevant confounders, mediators, moderators, mechanisms, colliders, and selection processes
* include competing structures or hypotheses
* represent different levels of biological or behavioral organization
* expose uncertainty and evidentiary support
* be revised by researchers
* contribute reviewed refinements back to the repository
* be translated into DAGs, Structural Causal Models, Bayesian Networks, Probabilistic Graphical Models, or other appropriate representations

Research Models Do Not

Research models do not independently redefine canonical knowledge merely because a researcher has drawn or modified a graph.

Changes intended to alter shared knowledge must pass through the Models4PT curation and provenance process.

⸻

6. Clinical Inference Engine

Role

The Clinical Inference Engine (CIE) is the reasoning infrastructure that transforms appropriate population-level knowledge into patient-specific explanatory and probabilistic models.

It is separate from Models4PT.

Models4PT constructs and curates population knowledge.

The CIE reasons with that knowledge in relation to an individual patient or other specific case.

The CIE Consumes

The CIE may consume from Models4PT:

* causal knowledge
* ontology information
* mechanisms
* population relationships
* probability information
* uncertainty
* contextual conditions
* provenance
* evidence
* model versions
* relevant subsets of the knowledge repository

Models4PT should expose these resources without requiring the CIE to depend on Models4PT’s internal implementation.

The CIE Owns

The CIE is responsible for:

* patient-specific model instantiation
* incorporation of individual patient findings
* incorporation of patient history
* incorporation of measurements and observations
* incorporation of patient context
* incorporation of patient goals
* temporal reasoning
* probabilistic inference
* Bayesian updating
* hypothesis comparison
* diagnostic reasoning
* prognosis-related reasoning
* treatment-related reasoning
* uncertainty propagation at the patient level
* updating patient models as new observations become available
* generating inspectable explanations of its reasoning

The CIE Does Not Own

The CIE does not own:

* the canonical scientific ontology
* the canonical population causal knowledge repository
* literature curation
* acceptance or rejection of scientific causal assertions
* the scientific provenance record maintained by Models4PT

Patient-specific inference must not silently modify canonical population knowledge.

Evidence generated from patient-level use may eventually motivate research or repository revision, but such revision must occur through the Models4PT scientific curation process.

⸻

7. Boundary Between Models4PT and the CIE

The primary boundary is:

Models4PT: Scientific literature and research knowledge → curated population causal knowledge

Clinical Inference Engine: Population causal knowledge + individual patient information → patient-specific causal and probabilistic reasoning

Models4PT should know enough about future inference requirements to represent population knowledge in a form that the CIE can use.

The CIE should not require Models4PT to perform patient reasoning on its behalf.

The systems therefore share a scientific language while retaining separate responsibilities.

⸻

8. Interface Between Models4PT and the CIE

The Models4PT–CIE interface must preserve scientific meaning.

When knowledge crosses this boundary, it should be possible to retain:

* concept identity
* causal structure
* mechanisms
* applicable populations and contexts
* measurements
* uncertainty
* probabilities when available
* provenance
* supporting and conflicting evidence
* assumptions
* knowledge version
* ontology version

The interface should allow the CIE to request only the portions of population knowledge relevant to a particular reasoning problem.

The interface must not depend on a particular graphical visualization format such as DAGitty.

The canonical representation should be richer than any single export or visualization format.

⸻

9. Downstream Applications

Role

Applications sit above Models4PT and/or the Clinical Inference Engine and provide workflows for particular users and problems.

Applications consume infrastructure. They should not become the canonical source of scientific knowledge or inference methodology.

Research Applications May Use

Models4PT directly for purposes such as:

* causal model development
* evidence synthesis
* study planning
* systematic review support
* hypothesis generation
* evidence auditing
* causal graph construction
* research education

Clinical Applications May Use

The Clinical Inference Engine for purposes such as:

* clinical reasoning assistance
* explanation of competing hypotheses
* prognosis support
* treatment planning support
* patient education
* shared decision support
* documentation support

Educational Applications May Use

Models4PT, the CIE, or both for purposes such as:

* interactive causal models
* causal reasoning education
* simulation
* tutoring
* clinical reasoning exercises
* competency assessment

Applications Do Not Own

Applications should not become the authoritative location for:

* canonical ontology definitions
* canonical scientific causal assertions
* scientific provenance
* population knowledge integration
* core patient-specific inference algorithms

Those responsibilities belong to the underlying infrastructure.

⸻

10. AI Boundary

AI is a capability used within the ecosystem, not the scientific authority.

Within Models4PT, AI may assist with:

* literature interpretation
* candidate knowledge extraction
* concept identification
* ontology alignment
* causal relation extraction
* mechanism extraction
* evidence comparison
* identification of related existing knowledge
* candidate model construction
* scientific critique

AI-generated scientific content remains candidate knowledge until appropriately reviewed.

Within future reasoning systems, AI may also assist with interaction, explanation, or other tasks, but it must not obscure the distinction between:

* source evidence
* curated scientific knowledge
* formal inference
* AI interpretation
* human judgment

⸻

11. This ChatGPT Project

Role

The Clinical Inquiry Platform ChatGPT Project is a development workspace and AI collaborator.

It is not Models4PT, the Clinical Inference Engine, the ontology, or the deployed scientific repository.

Its role is to assist with:

* scientific research
* conceptual development
* architecture
* critique
* software engineering
* data modeling
* ontology development
* causal modeling
* documentation
* testing
* implementation
* maintenance of conceptual continuity during development

Final scientific and architectural authority remains with the human investigator.

The design recommendations made within this workspace must remain subordinate to the Foundational Principles and established System Boundaries.

⸻

12. Boundary Rule for Future Decisions

When a new capability is proposed, first determine which layer owns the responsibility.

A useful test is:

Is this about constructing and curating population scientific knowledge?
It belongs primarily in Models4PT.

Is this about transforming population knowledge into reasoning about a particular patient or case?
It belongs primarily in the Clinical Inference Engine.

Is this about delivering a workflow or experience to a particular class of users?
It belongs primarily in an application.

Is this about the philosophical or epistemological justification for how knowledge and reasoning should work?
It belongs primarily in Clinical Inquiry.

If a capability crosses these boundaries, the systems should communicate through explicit interfaces rather than collapsing their responsibilities into a single application.

⸻

Closing Statement

The Clinical Inquiry Platform should develop as a set of interoperable but conceptually distinct layers:

Clinical Inquiry
provides the scientific and philosophical foundation.

↓

Models4PT
builds and curates computable population causal knowledge.

↓

Clinical Inference Engine
instantiates and reasons with that knowledge for individual patients or specific cases.

↓

Applications
provide research, educational, clinical, and other user-facing workflows.

The ontology and causal knowledge repository form essential parts of the Models4PT scientific infrastructure, while explicit interfaces allow that knowledge to support reasoning systems without sacrificing provenance, scientific meaning, transparency, or modularity.