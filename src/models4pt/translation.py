from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .domain import Evidence, ProposedCausalClaim, Source, Variable
from .extraction import CandidateExtraction, RelationshipType


class OntologyResolver:
    def resolve_variable(self, extracted_term: str) -> Optional[Variable]:
        raise NotImplementedError


class InMemoryOntologyResolver(OntologyResolver):
    def __init__(self, mapping: dict[str, Variable]) -> None:
        self.mapping = mapping

    def resolve_variable(self, extracted_term: str) -> Optional[Variable]:
        return self.mapping.get(extracted_term)


@dataclass
class EndpointResolution:
    extracted_term: str
    resolved_variable: Optional[Variable] = None

    @property
    def is_resolved(self) -> bool:
        return self.resolved_variable is not None


@dataclass
class CandidateTranslation:
    extraction_id: str
    source: Source
    evidence: Evidence
    cause_resolution: EndpointResolution
    effect_resolution: EndpointResolution
    proposed_claim: Optional[ProposedCausalClaim]
    notes: Optional[str] = None


def translate_candidate_extraction(
    extraction: CandidateExtraction,
    source_id: str,
    source_title: str,
    resolver: OntologyResolver,
) -> CandidateTranslation:
    source = Source(
        source_id=source_id,
        title=source_title,
        source_type="extracted-passage",
        description=f"AI extraction from passage reference: {extraction.passage_reference}",
    )
    evidence = Evidence(
        evidence_id=f"evidence-{extraction.extraction_id}",
        description=extraction.supporting_text,
        source=source,
    )

    cause_resolution = EndpointResolution(
        extracted_term=extraction.candidate_cause,
        resolved_variable=resolver.resolve_variable(extraction.candidate_cause),
    )
    effect_resolution = EndpointResolution(
        extracted_term=extraction.candidate_effect,
        resolved_variable=resolver.resolve_variable(extraction.candidate_effect),
    )

    proposed_claim = None
    if extraction.relationship_type == RelationshipType.CAUSAL:
        if cause_resolution.is_resolved and effect_resolution.is_resolved:
            if cause_resolution.resolved_variable.variable_id != effect_resolution.resolved_variable.variable_id:
                proposed_claim = ProposedCausalClaim(
                    proposal_id=f"proposal-{extraction.extraction_id}",
                    cause=cause_resolution.resolved_variable,
                    effect=effect_resolution.resolved_variable,
                    evidence=[evidence],
                )
                notes = "Resolved both endpoints and produced a candidate ProposedCausalClaim."
            else:
                notes = "Both endpoints resolved to the same variable identity; no ProposedCausalClaim created."
        else:
            notes = (
                "Extraction was causal but one or more endpoints remain unresolved; no ProposedCausalClaim created."
            )
    else:
        proposed_claim = None
        notes = (
            "No candidate ProposedCausalClaim produced because the extraction was not explicitly causal."
            if extraction.relationship_type in (RelationshipType.ASSOCIATIONAL, RelationshipType.UNCERTAIN)
            else "No translation was possible."
        )

    return CandidateTranslation(
        extraction_id=extraction.extraction_id,
        source=source,
        evidence=evidence,
        cause_resolution=cause_resolution,
        effect_resolution=effect_resolution,
        proposed_claim=proposed_claim,
        notes=notes,
    )
