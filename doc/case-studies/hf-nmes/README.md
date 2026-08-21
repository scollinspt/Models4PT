# Case Study: Heart Failure + NMES

A worked example carrying one clinical question end-to-end through the full
intended pipeline: draft population model (Synthesis) → refined via the
Models4PT workflow → instantiated for a patient by the Clinical Inference
Engine (CIE, not yet built) → dynamic clinical inquiry/reasoning for that
patient.

## Why this case study
- Companion/follow-up to "From Population Models to Patient Reasoning:
  Instantiation and Dynamic Clinical Inquiry."
- Clinical question: when is neuromuscular electrical stimulation (NMES)
  indicated or contraindicated for a particular heart failure (HF) patient,
  when the HF clinical practice guideline (CPG) recommends NMES as an
  intervention but current research evidence doesn't give patient-level
  guidance on when to use it?
- Purpose is dual:
  1. Concrete demonstration — makes the abstract Models4PT/CIE workflow
     legible to colleagues/students who understand the general idea but not
     the mechanics, so they can meaningfully contribute.
  2. Requirements discovery — using a real (if sparse) draft model exposes
     what Models4PT actually needs to do (representation, refinement,
     provenance) to produce something the CIE can instantiate for a patient.

## Relationship to the rest of the repo
This folder holds case-study content (narrative, source papers, the draft
model, instantiation/reasoning traces) — not governing principles
(`doc/project-foundation/`) and not the Models4PT implementation (`src/`).
Where useful, this case study exercises the actual `src/models4pt` code to
test whether the workflow holds up end-to-end; note in `notes.md` when it
does not, so gaps can feed back into the roadmap.

## Structure
- `synthesis/` — prior writings and the draft causal model as originally
  conceived (source material, treated as input, not edited in place).
- `model/` — the HF/NMES model as it is reviewed/refined through the
  Models4PT workflow (concepts, variables, claims, evidence, curation
  decisions — using the Stage 1 domain objects where applicable).
- `instantiation/` — patient-specific instantiation and the reasoning trace
  produced when the model is applied to a case, i.e. the proto-CIE step.
- `notes.md` — running log of what this example reveals is missing/needed
  from Models4PT and CIE, and open scientific/design questions.

## Status
Scaffolding only. Draft model and source papers not yet added.
