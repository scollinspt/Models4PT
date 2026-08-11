from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class RelationshipType(Enum):
    CAUSAL = "causal"
    ASSOCIATIONAL = "associational"
    UNCERTAIN = "uncertain"


@dataclass
class CandidateExtraction:
    extraction_id: str
    source_text: str
    passage_reference: Optional[str]
    candidate_cause: str
    candidate_effect: str
    relationship_type: RelationshipType
    supporting_text: str
    confidence: float
    notes: Optional[str] = None

    @property
    def is_candidate_causal_claim(self) -> bool:
        return self.relationship_type == RelationshipType.CAUSAL


def mock_extract_candidate_claim(
    extraction_id: str,
    source_text: str,
    passage_reference: Optional[str] = None,
) -> CandidateExtraction:
    normalized = source_text.lower()
    relationship_type = RelationshipType.UNCERTAIN
    notes = None

    if any(denial in normalized for denial in ["causality was not established", "not causal", "no evidence of causality"]):
        relationship_type = RelationshipType.ASSOCIATIONAL
        notes = "Text explicitly denies causal certainty and was classified as associational."
    elif any(keyword in normalized for keyword in ["causes", "cause", "led to", "leads to", "resulted in", "resulted from"]):
        if any(assoc in normalized for assoc in ["associated with", "correlated with", "linked to"]):
            relationship_type = RelationshipType.ASSOCIATIONAL
            notes = "Contains both causal and associational wording; classified conservatively as associational."
        else:
            relationship_type = RelationshipType.CAUSAL
            notes = "Text contains causal wording and was classified as a candidate causal relationship."
    elif any(keyword in normalized for keyword in ["reduced", "increased"]):
        relationship_type = RelationshipType.ASSOCIATIONAL
        notes = "Text contains outcome-related wording without explicit causality; classified as associational."
    elif any(assoc in normalized for assoc in ["associated with", "correlated with", "linked to"]):
        relationship_type = RelationshipType.ASSOCIATIONAL
        notes = "Text contains associational wording and was classified as a non-causal candidate relationship."
    else:
        relationship_type = RelationshipType.UNCERTAIN
        notes = "Relationship wording was ambiguous or uncertain."

    candidate_cause, candidate_effect = _extract_candidate_terms(source_text)
    confidence = 0.85 if relationship_type == RelationshipType.CAUSAL else 0.65 if relationship_type == RelationshipType.ASSOCIATIONAL else 0.45

    return CandidateExtraction(
        extraction_id=extraction_id,
        source_text=source_text,
        passage_reference=passage_reference,
        candidate_cause=candidate_cause,
        candidate_effect=candidate_effect,
        relationship_type=relationship_type,
        supporting_text=source_text,
        confidence=confidence,
        notes=notes,
    )


def _extract_candidate_terms(source_text: str) -> tuple[str, str]:
    import re

    lower = source_text.lower()
    patterns = [
        (r"(?P<cause>[\w\s\-]+?)\s+caused\s+(?:a |an |the )?(?P<effect>[\w\s\-]+)", True),
        (r"(?P<cause>[\w\s\-]+?)\s+causes\s+(?:a |an |the )?(?P<effect>[\w\s\-]+)", True),
        (r"(?P<cause>[\w\s\-]+?)\s+led to\s+(?:a |an |the )?(?P<effect>[\w\s\-]+)", True),
        (r"(?P<cause>[\w\s\-]+?)\s+leads to\s+(?:a |an |the )?(?P<effect>[\w\s\-]+)", True),
        (r"(?P<cause>[\w\s\-]+?)\s+resulted in\s+(?:a |an |the )?(?P<effect>[\w\s\-]+)", True),
        (r"(?P<cause>[\w\s\-]+?)\s+associated with\s+(?P<effect>[\w\s\-]+)", False),
        (r"(?P<cause>[\w\s\-]+?)\s+correlated with\s+(?P<effect>[\w\s\-]+)", False),
        (r"(?P<cause>[\w\s\-]+?)\s+linked to\s+(?P<effect>[\w\s\-]+)", False),
    ]

    for pattern, causal in patterns:
        match = re.search(pattern, lower)
        if match:
            cause_phrase = match.group("cause").strip()
            effect_phrase = match.group("effect").strip()
            return _normalize_candidate_term(cause_phrase, is_cause=True), _normalize_candidate_term(effect_phrase, is_cause=False)

    return "unknown", "unknown"


def _normalize_candidate_term(term: str, is_cause: bool) -> str:
    stopwords = {"a", "an", "the", "in", "of", "with", "and", "or", "to", "was", "were", "is", "are", "significant", "significantly", "reduced", "increased", "decreased", "major", "minor", "small", "large"}
    tokens = [token.strip(".,") for token in term.split() if token.strip(".,")]
    if not tokens:
        return "unknown"
    if is_cause:
        for token in reversed(tokens):
            if token not in stopwords:
                return token
        return tokens[-1]
    for token in tokens:
        if token not in stopwords:
            return token
    return tokens[0]
