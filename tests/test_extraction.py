import pytest

from models4pt.extraction import (
    CandidateExtraction,
    RelationshipType,
    mock_extract_candidate_claim,
)


def test_explicitly_causal_statement_produces_candidate_causal_relationship():
    source = "In this trial, the intervention caused a significant reduction in pain."
    extraction = mock_extract_candidate_claim("e1", source, passage_reference="Section 3")

    assert extraction.relationship_type == RelationshipType.CAUSAL
    assert extraction.is_candidate_causal_claim is True
    assert extraction.candidate_cause == "intervention"
    assert extraction.candidate_effect == "reduction"
    assert extraction.supporting_text == source
    assert extraction.passage_reference == "Section 3"


def test_purely_associational_statement_does_not_silently_become_causal():
    source = "The study found that pain was associated with decreased mobility."
    extraction = mock_extract_candidate_claim("e2", source, passage_reference="Abstract")

    assert extraction.relationship_type == RelationshipType.ASSOCIATIONAL
    assert extraction.is_candidate_causal_claim is False


def test_supporting_source_text_remains_attached():
    source = "Participants reported that sleep quality was correlated with balance impairment."
    extraction = mock_extract_candidate_claim("e3", source)

    assert extraction.supporting_text == source
    assert extraction.source_text == source
    assert extraction.passage_reference is None


def test_confidence_is_distinct_from_scientific_uncertainty():
    source = "The intervention led to reduced inflammation, but causality was not established."
    extraction = mock_extract_candidate_claim("e4", source)

    assert isinstance(extraction.confidence, float)
    assert extraction.confidence == 0.65
    assert extraction.relationship_type == RelationshipType.ASSOCIATIONAL
    assert extraction.notes is not None
    assert "classified" in extraction.notes
