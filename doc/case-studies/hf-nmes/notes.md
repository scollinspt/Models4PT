# Notes: HF/NMES Case Study

Running log of open questions and gaps discovered while working this example.
Not a governing doc — informal working notes.

## Open questions
- (none currently open — `ES` = Electrical Stimulation (NMES) and `AT` =
  Aerobic Training confirmed by project author.)

## Gaps this example exposes in Models4PT
- Model 4D's 27 DAGitty edges translate cleanly into 27
  `ProposedCausalClaim`s (17 variables, no id collisions), but every claim
  has to be created with an empty `evidence` list — DAGitty has no concept
  of evidence, citation, or per-edge justification, only structure. Stage 1
  domain objects already tolerate this (`evidence` defaults to `[]`), but
  there's currently no workflow step for *later* attaching evidence/sources
  to a claim that already exists, nor any status distinguishing "structural
  hypothesis with no evidence yet" from "reviewed/curated claim." That
  distinction will matter once curation begins on this model.
- No representation yet for *why* an edge was drawn (mechanism, direction of
  effect, expected magnitude) — DAGitty edges are unsigned/unqualified, and
  the Stage 1 `ProposedCausalClaim` doesn't currently capture qualification
  either (this may be intentional for now, but worth tracking against what
  the CIE will need to reason about a specific patient).
- Related to the above: no way to distinguish *Real* (mechanisms), *Actual*
  (events), and *Empirical* (experiences) for a given `Variable` — Bhaskar's
  critical realism domains (source: `synthesis/Realist Theory of Science.pdf`;
  also *Dictionary of Critical Realism*). These are **nested**, not parallel
  categories: Empirical ⊆ Actual ⊆ Real — every experience is of an event,
  every event is (or is produced by) a mechanism, but not every mechanism
  produces an event, and not every event is experienced/measured. Scientific
  and technological progress is what pulls more of the Real into the Actual,
  and more of the Actual into the Empirical. This was explored once before,
  in the DAGitty era of the project (`archive/CR_Variable_Plan.md`), but
  never carried into Stage 1, and that earlier plan treated the domains as
  three separate tag values rather than nested depths of the same referent —
  worth not repeating that framing here.
  Working implication: a `Variable`/`Concept` represents a claim about a Real
  mechanism by default; an `Observation` (not yet in Stage 1) would represent
  that mechanism's state having become Actual for a specific patient/time;
  a `Measurement`/`MeasurementResult` (partially in Stage 1) would represent
  that occurrence having become Empirical. In progress — see session
  discussion.
- The instantiation problem (per "From Population Knowledge to Patient
  Reasoning," synthesis/PopKnowledgePatientReasoning.pdf) means a single flat
  `ES -> Muscle_Function` claim can't be instantiated as-is: a population
  effect can arise from patients in heterogeneous causal configurations, so
  the generic model needs to represent *which* mechanisms could produce an
  effect, the enabling/moderating conditions under which each is operative,
  and the patient-observable indicators diagnostic of each. Tracing `ES`'s
  descendants in model 4D shows this isn't confined to one edge: `ES` casts
  a causal shadow over 10 of 17 nodes (`muscle_function`, `av_o2`,
  `anaerobic_threshold`, `vo2_max`, `bio_physio_status`, `symptom_status`,
  `six_mwd`, `functional_status`, `health_perception`, `hrqol`), converging
  at several points with independent (non-ES) contributors: `cardiac_output`
  (into `vo2_max`), `balance`/`gait_speed`/`mechanical_efficiency` (into
  `six_mwd`), and `social` (into `functional_status`/`hrqol`). Whether NMES
  matters for a given patient depends on whether their limitation is
  dominated by the ES-driven pathway or by one of these parallel ones — the
  concrete form of "heterogeneous causal configurations" in this model.
  Decision: first worked example of this enrichment will focus on the
  `six_mwd` convergence point (ES-driven: `anaerobic_threshold`; independent:
  `balance`, `gait_speed`, `mechanical_efficiency`), not `hrqol` (deferred as
  too fuzzy/multiply-determined for a first pass). To be prototyped locally
  in this case study (not `src/models4pt/domain.py`) before considering it
  for Stage 2.

## Gaps this example exposes in CIE (not yet built)
- (to fill in once instantiation is attempted)

## Session log — 2026-08-21: red pathway enrichment + quadrant system

**Where we left off / how to resume:** we were mid-design on enriching the
red (`ES`-driven) mechanism to `six_mwd` with intermediary Real-mechanism
nodes, tagged by how far each currently reaches into Actual/Empirical. No
code changes have been made for this section yet — `mechanisms.py` still
only has the four coarse pathways from the prior session. Next concrete
step on return: formalize both `ES -> Strength` and `ES -> Endurance` as
separate branches (see below) as new intermediary variables/claims, still
scoped locally to this case study, not `domain.py`.

**Strength vs. Endurance split (confirmed reasoning, not yet implemented):**
`Muscle_Function` should split into **Strength** (force-generating capacity)
and **Endurance** (ability to sustain/repeat contractions), related but
distinct: sustainable duration/reps is inversely related to %MVC used
(force–endurance/force–duration relationship), and sustained contractions
above roughly ~30% MVC progressively occlude intramuscular blood flow,
accelerating fatigue, whereas duty-cycled contractions (e.g. 1s on/10s off)
allow reperfusion and can be sustained much longer. This makes **NMES
stimulation parameters (intensity relative to strength, duty cycle) a
clinically controllable lever** directly relevant to which mechanism
(Strength vs. Endurance) is engaged — not just an intermediary detail.

**Correction: `ES` does not target only Endurance/Quadrant C.** `ES` has (at
least) two distinct mechanism targets depending on patient context:
- `ES -> Strength` (Attain-oriented): used when a patient can't yet attain
  sufficient force-generating capacity to perform active exercise at all —
  NMES as a bridge/enabling intervention (likely higher intensity, lower
  duty cycle).
- `ES -> Endurance` (Sustain-oriented): used when the patient can attain
  adequate force but can't sustain repeated/prolonged effort (likely lower
  intensity, higher duty cycle, more reps).
Which branch is the actual therapeutic target for a given patient depends on
which quadrant they're in (see below) — this is the intervention-side
analogue of the "heterogeneous causal configurations" problem already noted
for the outcome side (six_mwd's competing mechanisms).

**Quadrant system connection (major finding).** Author added course materials
to `synthesis/`: `PCM5 - Quadrants.png`, `PCM5 Algorithm.png`,
`Quadrant-Pathway-ThoughtProcess_1.5.png`, `Quadrant_Thought_Process_1.0.png`,
`Quadrants_1.pdf`, `HF-CPG-Algorithm.png` — the clinical reasoning system
taught in the author's cardiopulmonary PT course (PCM 5), independently
developed but stemming from the same underlying reasoning system as this
causal model (author's own observation). Key structure:
- Two axes: **Attain vs. Sustain** (cannot generate enough force/skill vs.
  cannot sustain/repeat effort) and **Reversible vs. Not Reversible**, further
  split by **disease-specific vs. not disease-specific** impairment.
- Quadrant A (reversible, cannot Attain): Strength, Coordination, Balance,
  Motor control/skill, Functional training.
- Quadrant C (reversible, cannot Sustain): Aerobic Conditioning, Endurance
  training — explicitly lists NMES, IMT, BFR. (Author's correction: NMES is
  NOT confined to Quadrant C — see Strength/Endurance split above.)
- `HF-CPG-Algorithm.png`'s "Signs of Exertional Intolerance" box (chest pain,
  abnormal vital sign response, new pulmonary crackles, new S3, new
  arrhythmia) is a real, bedside-accessible Empirical indicator set for
  judging disease-specific (cardiac) limitation — better than the
  CPET/echo differentiator drafted earlier for the "cardiac" mechanism in
  `mechanisms.py`; **should replace it** when we get back to that.
- Open design question (not yet resolved): is the quadrant algorithm the
  CIE-side instantiation procedure itself (a reasoning process to design
  later), or does it also reveal new Real-level variables/moderators
  missing from model 4D entirely (e.g. a node for Attain-vs-Sustain
  limitation type, and one for disease-specific-vs-not)? Leaning toward
  "both" but not yet decided.

**Concrete next steps when resuming:**
1. Decide how "Attain vs. Sustain" and "disease-specific vs. not" should be
   represented — as new `Variable`s in model 4D, as moderators on
   `ProposedMechanism`, or as part of future CIE-side instantiation logic.
2. Replace the draft "cardiac" mechanism's differentiating measurement with
   the Signs of Exertional Intolerance indicators from `HF-CPG-Algorithm.png`.
3. Formalize `ES -> Strength` and `ES -> Endurance` as distinct branches
   (new intermediary variables + claims), each with duty-cycle/intensity as
   a contributing factor.
4. Only after the above: return to fleshing out intermediary physiological
   nodes between `ES`/`Strength`/`Endurance` and `Anaerobic_Threshold` (blood
   flow/occlusion, oxidative capacity, ventilatory threshold — drafted
   candidates in prior discussion, not yet in code, still need author
   correction/citation).
