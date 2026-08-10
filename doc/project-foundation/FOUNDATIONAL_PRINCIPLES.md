FOUNDATIONAL PRINCIPLES

Purpose

These principles define the enduring philosophy and constraints of the Models4PT project. They are intended to remain stable as the software, architecture, and implementation evolve. When design decisions are made, they should be evaluated against these principles. If a proposed feature conflicts with a foundational principle, the principle takes precedence unless it is intentionally revised.

⸻

Principle 1. The Canonical Product is Curated Causal Knowledge

The canonical product of Models4PT is curated causal knowledge, not causal diagrams.

The repository is the primary product of the system. Research models are views of that repository. Graphical representations (e.g., DAGs) are exports or visualizations of the underlying knowledge rather than the knowledge itself. The Clinical Inference Engine (CIE) reasons over the curated repository rather than over individual diagrams.

⸻

Principle 2. Researchers Remain the Scientific Authority

Every causal assertion must remain explicitly attributable, reviewable, and revisable by humans.

Models4PT is an AI-assisted knowledge engineering environment. AI proposes candidate causal knowledge, but researchers remain responsible for evaluating, accepting, modifying, or rejecting those proposals. Every accepted causal assertion should retain transparent provenance, including its supporting evidence, contributors, reviewers, rationale, confidence, competing explanations, and revision history.

⸻

Principle 3. Shared Meaning Before Shared Knowledge

Every concept entering the repository must be semantically reconciled with the existing ontology before becoming part of the canonical knowledge base.

The long-term value of the repository depends on consistent conceptual meaning. Before new variables, constructs, or mechanisms become part of the shared repository, they must be evaluated against existing concepts to determine whether they represent an existing concept, a subtype, a measurement, a related construct, or a genuinely new concept. This prevents semantic fragmentation while preserving scientific nuance.

⸻

Principle 4. Distinguish Scientific Objects

Concepts, measurements, mechanisms, causal relationships, and evidence are distinct scientific objects and must never be conflated.

A theoretical construct is not the same as its measurement. A measurement is not the same as a causal mechanism. Evidence supporting a relationship is not the relationship itself. Maintaining these distinctions is essential for scientific rigor, ontology development, and reliable causal reasoning.

⸻

Principle 5. Knowledge Evolves Through Refinement

Scientific knowledge is accumulated through refinement rather than replacement.

New evidence should enrich the repository by supporting, contradicting, qualifying, extending, or contextualizing existing causal knowledge. The repository should preserve the evolution of scientific understanding rather than overwrite previous work. Models4PT is intended to represent the development of knowledge over time.

⸻

Principle 6. AI Produces Candidate Knowledge, Not Scientific Conclusions

AI-generated outputs are candidate scientific interpretations requiring human evaluation.

Models4PT may extract variables, mechanisms, causal relationships, or entire candidate models from literature or other sources. These outputs represent the AI’s interpretation of the available evidence and should never be considered authoritative until reviewed by researchers.

⸻

Principle 7. Separation of Knowledge Construction and Knowledge Reasoning

Models4PT constructs causal knowledge. The Clinical Inference Engine reasons with causal knowledge.

Models4PT exists primarily for researchers to build, curate, and refine the causal knowledge repository. The Clinical Inference Engine is a separate system that consumes this repository to perform patient-specific or question-specific reasoning. Maintaining this separation allows each system to evolve independently while preserving a common scientific foundation.

⸻

Principle 8. Scientific Transparency Over Automation

Every meaningful scientific conclusion produced by the system should be explainable, traceable, and reproducible.

Automation should increase efficiency without obscuring scientific reasoning. Users should always be able to inspect the evidence, assumptions, ontology mappings, causal pathways, and reasoning steps that led to a recommendation, model, or inference.

⸻

Closing Statement

Models4PT is not intended to replace scientific reasoning. Its purpose is to assist researchers in constructing a transparent, continually evolving, and scientifically defensible causal knowledge repository. That repository serves as the foundation for future causal modeling, evidence synthesis, education, and clinical inference across the broader Clinical Inquiry Platform.