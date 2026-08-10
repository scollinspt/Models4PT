Models4PT Research Program

Building a Computational Science of Physical Therapy Knowledge

Mission

Models4PT is a long-term research program whose objective is to develop a computational representation of physical therapy knowledge. Rather than viewing scientific publications as isolated sources of evidence, Models4PT seeks to represent accumulated scientific understanding as an evolving collection of computable causal models that can be integrated, queried, refined, and ultimately instantiated for reasoning about individual patients.

The project combines philosophy of science, causal inference, knowledge representation, biomedical ontologies, graph theory, probabilistic modeling, and modern software engineering to create an open platform for scientific knowledge.

The guiding question is simple:

What do we collectively know about physical therapy?

Answering that question requires building representations that are richer than traditional evidence summaries. The aim is to represent mechanisms, causal structure, uncertainty, competing hypotheses, and provenance in forms that can be interpreted by both humans and machines.

⸻

Relationship to Clinical Inquiry

The Clinical Inquiry project establishes the philosophical foundations for translating population-level scientific knowledge into reasoning about individual patients. It argues that clinical reasoning requires the construction of patient-specific explanatory representations through a process of instantiation.

Models4PT addresses the complementary problem.

Rather than asking how knowledge is instantiated for a patient, it asks how scientific knowledge itself should be represented before instantiation becomes possible.

The projects therefore operate at different levels.

Clinical Inquiry

* Population knowledge → Patient reasoning

Models4PT

* Scientific literature → Population knowledge

Future clinical reasoning systems will use Models4PT as their population knowledge layer.

⸻

Scientific Premise

Scientific knowledge does not exist primarily as papers.

It exists as an evolving understanding of biological systems.

Publications are observations about that understanding.

The purpose of Models4PT is to recover the underlying causal structure from scientific literature and represent it explicitly.

In this view, every study contributes evidence toward refining a shared model rather than standing as an isolated fact.

⸻

Long-Term Vision

Develop an open computational knowledge base representing physical therapy science as a hierarchy of interconnected causal models.

Each model should include

* biological entities
* measurable variables
* causal relationships
* interventions
* outcomes
* uncertainty
* supporting evidence
* provenance
* competing explanations

The resulting knowledge base should support

* evidence synthesis
* hypothesis generation
* education
* systematic reviews
* computational research
* patient-specific reasoning engines

⸻

Core Scientific Questions

Knowledge Representation

How should physical therapy knowledge be represented computationally?

⸻

Causal Structure

How should mechanisms be encoded?

What constitutes a causal explanation within rehabilitation science?

⸻

Knowledge Integration

How should findings from multiple publications be combined?

How should conflicting evidence be represented rather than discarded?

⸻

Uncertainty

How should uncertainty propagate through integrated causal models?

⸻

Hierarchical Organization

How should molecular, physiological, biomechanical, behavioral, and environmental mechanisms be represented within nested causal systems?

⸻

Evolution of Knowledge

How should scientific knowledge change as new evidence becomes available?

⸻

Research Themes

Theme 1

Ontology

Develop a formal ontology describing

* anatomical structures
* physiological systems
* impairments
* movement
* interventions
* outcomes
* environmental constraints
* patient goals

⸻

Theme 2

Causal Modeling

Represent scientific mechanisms using

* Directed Acyclic Graphs
* Structural Causal Models
* Bayesian Networks
* Probabilistic Graphical Models

Investigate when each representation is most appropriate.

⸻

Theme 3

Knowledge Extraction

Develop methods for extracting computable causal knowledge from scientific publications.

Research questions include

* variable identification
* intervention recognition
* mechanism extraction
* causal language interpretation
* effect estimation
* uncertainty extraction

This work will combine natural language processing with human expert review.

⸻

Theme 4

Knowledge Integration

Construct methods for combining evidence across studies while preserving

* provenance
* confidence
* study quality
* uncertainty
* competing hypotheses
* version history

Rather than replacing disagreement with consensus, Models4PT should explicitly represent scientific disagreement.

⸻

Theme 5

Knowledge Repository

Develop an evolving repository in which scientific knowledge is represented as interconnected causal models rather than disconnected documents.

The repository should support

* querying
* visualization
* version control
* comparison
* evidence auditing
* collaborative development

⸻

Theme 6

Application Programming Interfaces

Expose knowledge through machine-readable APIs capable of supporting

* educational software
* research tools
* evidence synthesis
* computational modeling
* clinical reasoning engines

⸻

Mathematical Foundations

The development of Models4PT will require progressive mastery of several mathematical disciplines.

Graph Theory

Representation of causal structure.

Probability

Representation of uncertainty.

Bayesian Statistics

Evidence updating and probabilistic inference.

Information Theory

Measurement of information gained from scientific evidence and efficient representation of complex models.

Optimization

Model fitting and parameter estimation.

Dynamical Systems

Representation of change over time and adaptive biological behavior.

Control Theory

Modeling regulation and intervention.

Computational Geometry

Representation of anatomy and movement.

⸻

Software Architecture

The software platform will evolve through successive stages.

Stage 1

Knowledge extraction from scientific literature.

Stage 2

Construction of machine-readable causal graphs.

Stage 3

Integration across publications.

Stage 4

Versioned knowledge repository.

Stage 5

Query engine.

Stage 6

REST API.

Stage 7

Interactive visualization.

Stage 8

Support for external reasoning engines.

⸻

Development Philosophy

Models4PT should remain

* open source
* transparent
* reproducible
* version controlled
* evidence based
* extensible
* domain driven

Scientific knowledge should never become detached from its supporting evidence. Every relationship in the system should remain traceable to the publications from which it was derived.

⸻

Milestones

Phase I — Foundations

* Formal ontology
* Initial causal model specification
* Repository architecture
* Literature extraction pipeline

Phase II — Knowledge Integration

* Cross-study synthesis
* Provenance tracking
* Evidence weighting
* Versioned model repository

Phase III — Computational Infrastructure

* API development
* Interactive graph visualization
* Query language
* Collaboration tools

Phase IV — Scientific Applications

* Automated evidence synthesis
* Educational applications
* Research support
* Integration with downstream clinical reasoning systems

⸻

Ultimate Objective

The long-term objective of Models4PT is to establish a new form of scientific infrastructure for physical therapy. Instead of treating knowledge as a collection of publications, the project seeks to represent accumulated scientific understanding as a living network of computable causal models. This representation becomes the foundation upon which future systems—including patient-specific reasoning engines, predictive simulations, and decision-support tools—can be built while remaining transparent, explainable, and directly connected to the evidence from which they were derived.