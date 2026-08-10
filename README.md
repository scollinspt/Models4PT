# Models4PT

**Models4PT will be an open platform for constructing, integrating, and evolving computable causal representations of biomedical knowledge.**

Models4PT represents scientific knowledge as an evolving network of probabilistic causal models that can be synthesized across publications and ultimately instantiated for patient-specific reasoning, rather than treating individual research studies as isolated pieces of evidence.

Models4PT is designed to answer a single question:

> **What do we collectively know?**

It serves as the population knowledge layer for downstream reasoning systems, including Bayesian clinical reasoning engines that answer:

> **Given this patient, what does that knowledge imply?**

---

# Vision

Scientific knowledge accumulates as structured causal knowledge rather than disconnected publications.

Every research study contributes evidence toward refining a shared representation of biomedical mechanisms.

Models4PT provides the infrastructure to:

- Extract causal knowledge from scientific literature
- Construct graphical causal models
- Integrate evidence across multiple studies
- Track provenance and uncertainty
- Maintain versioned causal knowledge
- Expose population-level models through machine-readable APIs
- Support downstream patient-specific reasoning systems

The long-term goal is to build a continuously evolving computational representation of biomedical knowledge that supports transparent, explainable, and evidence-based reasoning.

---

# Project Architecture

```text
Scientific Literature
        │
        ▼
Knowledge Extraction
        │
        ▼
Causal Model Construction
        │
        ▼
Knowledge Integration
        │
        ▼
Models4PT Knowledge Repository
        │
        ▼
Models4PT API
        │
        ├───────────────┐
        ▼               ▼
Researchers      Clinical Applications
                     │
                     ▼
 Bayesian Clinical Reasoning Engine
                     │
                     ▼
 Patient-specific reasoning
```

Models4PT is **not** itself a clinical decision support system.

Instead, it provides the population-level causal knowledge that can be instantiated by downstream reasoning systems.

---

# Core Capabilities

## Knowledge Extraction

Automatically identify and extract:

- Variables
- Interventions
- Outcomes
- Mediators
- Moderators
- Confounders
- Effect estimates
- Causal assumptions
- Sources of uncertainty

from biomedical publications.

---

## Causal Model Construction

Create machine-readable causal models using graphical representations including:

- Directed Acyclic Graphs (DAGs)
- Bayesian Networks
- Structural Causal Models
- Probabilistic Graphical Models

---

## Knowledge Integration

Combine evidence across multiple publications while preserving:

- provenance
- evidence quality
- uncertainty
- conflicting evidence
- competing hypotheses
- version history

---

## Knowledge Repository

Maintain an evolving repository of biomedical knowledge consisting of:

- concepts
- variables
- causal relationships
- evidence
- effect estimates
- uncertainty
- provenance

rather than isolated research papers.

---

## API

Expose computable biomedical knowledge for:

- Clinical reasoning engines
- Research software
- Educational tools
- Evidence synthesis platforms
- Decision support systems

---

# Initial Application Domain

Initial development focuses on rehabilitation and physical therapy.

The underlying architecture is intentionally domain-independent and is designed to support broader biomedical knowledge representation as the platform matures.

---

# Planned Features

## Literature-to-Model Pipeline

- Import scientific publications
- LLM-assisted causal knowledge extraction
- Human review workflows
- Automatic generation of causal graphs

---

## Knowledge Integration

- Variable mapping
- Ontology alignment
- Evidence synthesis
- Confidence estimation
- Conflict resolution

---

## Hierarchical Models

Support hierarchical causal systems by allowing nodes to reference nested causal models.

This enables representation of:

- physiological subsystems
- biomechanical systems
- psychological models
- social determinants
- multiscale biological mechanisms

---

## Collaboration

Support collaborative scientific knowledge development through:

- version control
- provenance tracking
- contributor attribution
- peer review workflows
- model comparison
- evidence auditing

---

# Relationship to the Clinical Inference Engine

Models4PT and the Clinical Inference Engine serve complementary purposes.

| Models4PT | Clinical Reasoning Engine |
|-----------|------------------------------------|
| Population knowledge | Individual patient reasoning |
| Scientific evidence | Patient observations |
| Knowledge construction | Knowledge application |
| Causal model repository | Clinical inference |
| "What do we collectively know?" | "What does this imply for this patient?" |

---

# Origins

Models4PT was originally inspired by the pioneering work of **DAGitty** and the work of **Johannes Textor**, whose contributions demonstrated the value of graphical causal models for scientific reasoning and causal inference.

Early prototypes explored extending DAGitty for rehabilitation research.

As the project's vision evolved, Models4PT expanded beyond an interactive DAG editor into a broader platform for:

- causal knowledge extraction
- evidence integration
- provenance tracking
- versioned causal knowledge
- population-level model construction
- machine-readable biomedical knowledge

We gratefully acknowledge the DAGitty project as an important intellectual influence on the development of Models4PT.

---

# Technology Roadmap

Current priorities include:

- Python backend
- FastAPI services
- PostgreSQL knowledge repository
- Graph-based model representation
- LLM-assisted knowledge extraction
- Knowledge versioning
- REST API
- Interactive web interface
- Collaborative workflows

---

# Running the Current Prototype

```bash
git clone https://github.com/scollinspt/Models4PT.git
```

Open:

```
gui/dags.html
```

in a modern web browser.

The current repository contains early prototypes while the platform architecture continues to evolve.

---
# Theoretical Foundations

Models4PT is grounded in work from causal inference, probabilistic graphical modeling, philosophy of science, and biomedical knowledge representation.

Its architecture is informed by several complementary perspectives:

- Structural Causal Models and Directed Acyclic Graphs (Pearl, Greenland, Hernán, Textor)
- Bayesian reasoning and probabilistic graphical models
- Scientific model synthesis and knowledge integration
- Critical realism and mechanistic explanation
- The transition from population-level scientific knowledge to patient-specific clinical reasoning

The design of Models4PT is particularly motivated by the following publications:

- **Collins, S.M. (2026). _From Population Knowledge to Patient Reasoning._**

  https://philpapers.org/rec/COLFPK

- **Collins, S.M. (2018). _Synthesis: Causal Models, Causal Knowledge, and Scientific Representation._**

  *Cardiopulmonary Physical Therapy Journal.*

  https://doi.org/10.1097/CPT.0000000000000101

---

# Contact

**Sean M. Collins, PT, ScD**

GitHub: https://github.com/scollinspt

---

*Models4PT is an evolving open-source research project exploring causal knowledge representation, evidence synthesis, and computational clinical reasoning.*
