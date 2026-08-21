"""Population-level mechanism hypotheses for the ES -> ... -> 6MWD pathway in
model 4D (see ../notes.md for the full derivation).

A ProposedMechanism is Models4PT-side content: a claim about the *class* of
HF patients (that a distinguishable causal configuration exists, and that
the literature offers a way to measure which configuration a patient
belongs to) — not a rule for classifying any particular patient. Classifying
an individual patient using these differentiating measurements is the CIE's
job (patient instantiation), out of scope here.

These four mechanisms are drafts, not scientific conclusions — provided as
candidates for review/correction, consistent with AI output being candidate
knowledge only (see doc/project-foundation/FOUNDATIONAL_PRINCIPLES.md).
"""
from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[4]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from models4pt.domain import Evidence, Measurement, ProposedCausalClaim, Variable  # noqa: E402

from model_4d import build_claims, build_variables  # noqa: E402


@dataclass
class ProposedMechanism:
    """A candidate causal pathway to a shared effect, plus how the literature
    differentiates it from other pathways to the same effect. Resolved
    (references real Variables/Measurements) but not yet curated — parallels
    ProposedCausalClaim's position in the Stage 1 workflow.
    """
    mechanism_id: str
    effect: Variable
    pathway: list[ProposedCausalClaim]
    differentiating_measurements: list[Measurement]
    evidence: list[Evidence] = field(default_factory=list)
    notes: Optional[str] = None


def _claims_by_edge(claims: list[ProposedCausalClaim]) -> dict[tuple[str, str], ProposedCausalClaim]:
    return {(c.cause.variable_id, c.effect.variable_id): c for c in claims}


def build_six_mwd_mechanisms() -> list[ProposedMechanism]:
    variables = build_variables()
    claims = build_claims(variables)
    by_edge = _claims_by_edge(claims)

    def claim(cause_id: str, effect_id: str) -> ProposedCausalClaim:
        return by_edge[(variables[cause_id].variable_id, variables[effect_id].variable_id)]

    six_mwd = variables["six_mwd"]

    peripheral = ProposedMechanism(
        mechanism_id="mechanism-six_mwd-peripheral",
        effect=six_mwd,
        pathway=[
            claim("es", "muscle_function"),
            claim("muscle_function", "anaerobic_threshold"),
            claim("anaerobic_threshold", "six_mwd"),
        ],
        differentiating_measurements=[
            Measurement(
                measurement_id="measurement-peripheral-limitation",
                label="Lower-extremity strength testing / CPET peripheral-limitation pattern",
                variable=variables["muscle_function"],
                description="Draft: literature approach hypothesized to differentiate a "
                "peripheral/muscular-limited HF subgroup from other subgroups. Not yet confirmed.",
            )
        ],
        notes="Draft candidate mechanism — pending author review.",
    )

    cardiac = ProposedMechanism(
        mechanism_id="mechanism-six_mwd-cardiac",
        effect=six_mwd,
        pathway=[
            claim("cardiac_output", "vo2_max"),
            claim("vo2_max", "anaerobic_threshold"),
            claim("anaerobic_threshold", "six_mwd"),
        ],
        differentiating_measurements=[
            Measurement(
                measurement_id="measurement-cardiac-limitation",
                label="Echocardiographic ejection fraction / CPET central-limitation pattern",
                variable=variables["cardiac_output"],
                description="Draft: literature approach hypothesized to differentiate a "
                "cardiac/central-limited HF subgroup from other subgroups. Not yet confirmed.",
            )
        ],
        notes="Draft candidate mechanism — pending author review. Independent of ES.",
    )

    balance_gait = ProposedMechanism(
        mechanism_id="mechanism-six_mwd-balance_gait",
        effect=six_mwd,
        pathway=[
            claim("balance", "six_mwd"),
            claim("balance", "gait_speed"),
            claim("gait_speed", "six_mwd"),
        ],
        differentiating_measurements=[
            Measurement(
                measurement_id="measurement-balance-gait-limitation",
                label="Balance testing (e.g. Berg Balance Scale, Timed Up and Go)",
                variable=variables["balance"],
                description="Draft: literature approach hypothesized to differentiate a "
                "balance/gait-limited HF subgroup from other subgroups. Not yet confirmed.",
            )
        ],
        notes="Draft candidate mechanism — pending author review. Independent of ES.",
    )

    mechanical_efficiency = ProposedMechanism(
        mechanism_id="mechanism-six_mwd-mechanical_efficiency",
        effect=six_mwd,
        pathway=[
            claim("mechanical_efficiency", "six_mwd"),
        ],
        differentiating_measurements=[
            Measurement(
                measurement_id="measurement-mechanical-efficiency",
                label="Gait analysis / energy cost of walking",
                variable=variables["mechanical_efficiency"],
                description="Draft: literature approach hypothesized to differentiate a "
                "movement-inefficiency-limited HF subgroup from other subgroups. Not yet confirmed.",
            )
        ],
        notes="Draft candidate mechanism — pending author review. Independent of ES.",
    )

    return [peripheral, cardiac, balance_gait, mechanical_efficiency]


if __name__ == "__main__":
    mechanisms = build_six_mwd_mechanisms()
    for mechanism in mechanisms:
        print(f"{mechanism.mechanism_id}:")
        for c in mechanism.pathway:
            print(f"    {c.cause.label} -> {c.effect.label}")
        for measurement in mechanism.differentiating_measurements:
            print(f"    differentiator: {measurement.label}")
