"""Translation of model 4D (draft DAGitty causal diagram, see ``model4d_dagitty.txt``)
into Stage 1 Models4PT domain objects.

This is a direct construction from the DAGitty source, not a run through the
extraction/translation pipeline in ``models4pt.translation`` — that pipeline
assumes each candidate claim comes with its own supporting passage of text as
Evidence. Model 4D instead asserts a whole diagram's worth of edges at once,
with no evidence attached to any individual edge. That gap is the point: it
is exactly what plain DAGitty output does not give Models4PT, and part of
what this case study is meant to surface (see ../notes.md).

The two DAGitty "exposure" nodes are:
  - ES: Electrical Stimulation (the NMES intervention of interest).
  - AT: Aerobic Training (a comparator exposure).
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from models4pt.domain import Concept, ProposedCausalClaim, Source, Variable  # noqa: E402

MODEL_4D_SOURCE = Source(
    source_id="model4d-dagitty",
    title="Model 4D (draft causal diagram, HF/NMES synthesis)",
    source_type="prior-synthesis",
    description=(
        "Author's prior draft causal model, most complete of several DAGitty "
        "iterations toward a heart failure / NMES model. Represents possible "
        "causal connections only; carries no per-edge evidence or citations. "
        "See ../synthesis/ for source writings and ../model/model4d_dagitty.txt "
        "for the DAGitty code this was translated from."
    ),
)

# node_id -> (label, description)
_NODE_INFO: dict[str, tuple[str, str | None]] = {
    "av_o2": ("(a-v)O2", "Arteriovenous oxygen difference."),
    "six_mwd": ("6MWD", "Six-Minute Walk Distance/Test."),
    "at": ("AT", "Aerobic Training (comparator exposure)."),
    "anaerobic_threshold": ("Anaerobic_Threshold", None),
    "balance": ("Balance", None),
    "bio_physio_status": ("Bio/PhysioStatus", "Biological/physiological status."),
    "cardiac_output": ("Cardiac_Output", None),
    "es": ("ES", "Electrical Stimulation (the NMES intervention of interest)."),
    "functional_status": ("FunctionalStatus", None),
    "gait_speed": ("Gait_Speed", None),
    "hrqol": ("HRQOL", "Health-related quality of life."),
    "health_perception": ("HealthPerception", None),
    "mechanical_efficiency": ("Mechanical_Efficiency", None),
    "muscle_function": ("Muscle_Function", None),
    "social": ("Social", None),
    "symptom_status": ("SymptomStatus", None),
    "vo2_max": ("VO2_max", "Maximal oxygen uptake (VO2max)."),
}

# DAGitty edges (cause_node_id, effect_node_id), transcribed from model4d_dagitty.txt.
_EDGES: list[tuple[str, str]] = [
    ("av_o2", "vo2_max"),
    ("six_mwd", "functional_status"),
    ("at", "balance"),
    ("at", "cardiac_output"),
    ("at", "mechanical_efficiency"),
    ("at", "muscle_function"),
    ("anaerobic_threshold", "six_mwd"),
    ("balance", "six_mwd"),
    ("balance", "gait_speed"),
    ("bio_physio_status", "functional_status"),
    ("bio_physio_status", "symptom_status"),
    ("cardiac_output", "vo2_max"),
    ("es", "muscle_function"),
    ("functional_status", "hrqol"),
    ("gait_speed", "six_mwd"),
    ("health_perception", "hrqol"),
    ("mechanical_efficiency", "six_mwd"),
    ("muscle_function", "av_o2"),
    ("muscle_function", "anaerobic_threshold"),
    ("social", "functional_status"),
    ("social", "hrqol"),
    ("social", "health_perception"),
    ("symptom_status", "functional_status"),
    ("symptom_status", "hrqol"),
    ("symptom_status", "health_perception"),
    ("vo2_max", "anaerobic_threshold"),
    ("vo2_max", "bio_physio_status"),
]


def build_variables() -> dict[str, Variable]:
    variables: dict[str, Variable] = {}
    for node_id, (label, description) in _NODE_INFO.items():
        concept = Concept(concept_id=f"concept-{node_id}", label=label, description=description)
        variables[node_id] = Variable(
            variable_id=f"var-{node_id}",
            label=label,
            concept=concept,
            description=description,
        )
    return variables


def build_claims(variables: dict[str, Variable]) -> list[ProposedCausalClaim]:
    claims = []
    for index, (cause_id, effect_id) in enumerate(_EDGES, start=1):
        claims.append(
            ProposedCausalClaim(
                proposal_id=f"model4d-claim-{index:02d}",
                cause=variables[cause_id],
                effect=variables[effect_id],
                # No per-edge evidence exists in the DAGitty source — see module docstring.
                evidence=[],
            )
        )
    return claims


if __name__ == "__main__":
    vars_by_id = build_variables()
    claims = build_claims(vars_by_id)
    print(f"Variables: {len(vars_by_id)}")
    print(f"Claims: {len(claims)}")
    for claim in claims:
        print(f"  {claim.cause.label} -> {claim.effect.label}")
