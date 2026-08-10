from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Concept:
    """A semantic identity for a phenomenon, construct, or scientific concept.

    Scientific identity is grounded in meaning and ontology, not in the
    internal ID used by the software.
    """
    concept_id: str
    label: str
    description: Optional[str] = None


@dataclass
class Variable:
    """A specified aspect, property, state, quantity, occurrence, or condition
    whose states may differ and can therefore participate in causal representation.

    For this first experiment, each Variable references exactly one Concept.
    This is a deliberate simplification and may be revisited later.

    variable_id represents software/repository identity for this experiment.
    It does not settle scientific identity or the criteria for equivalence
    between two Variables.
    """
    variable_id: str
    label: str
    concept: Concept
    description: Optional[str] = None


@dataclass
class Measurement:
    """A specification of an empirical procedure, instrument, or method intended
    to provide information about a Variable.

    Measurements are not observations or observed values.
    """
    measurement_id: str
    label: str
    variable: Variable
    description: Optional[str] = None


@dataclass
class Source:
    """The origin of knowledge or data, such as a publication, dataset, or report."""
    source_id: str
    title: str
    source_type: Optional[str] = None
    description: Optional[str] = None


@dataclass
class Evidence:
    """A discrete scientific finding or evidentiary item derived from a Source.

    Evidence is neutral regarding whether it supports, contradicts, or qualifies
    a proposed claim.
    """
    evidence_id: str
    description: str
    source: Source
    measurement: Optional[Measurement] = None


@dataclass
class ProposedCausalClaim:
    """A proposed directional causal relation between two Variables.

    This first experiment limits claims to a single cause and a single effect.
    Rationale and justification are intentionally kept outside the claim itself.
    """
    proposal_id: str
    cause: Variable
    effect: Variable
    evidence: List[Evidence] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.cause.variable_id == self.effect.variable_id:
            raise ValueError("cause and effect must be distinct Variables")


@dataclass
class CurationDecision:
    """A human judgment about a ProposedCausalClaim.

    The decision itself is separate from the claim being evaluated.
    """
    decision_id: str
    proposal: ProposedCausalClaim
    reviewer: str
    rationale: Optional[str] = None
    decision_type: Optional[str] = None
