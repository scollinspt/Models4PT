import pytest

from models4pt.domain import Concept, ProposedCausalClaim, Variable
from models4pt.extraction import CandidateExtraction, RelationshipType
from models4pt.translation import InMemoryOntologyResolver, translate_candidate_extraction


def test_causal_extraction_translates_to_candidate_proposed_causal_claim():
    extraction = CandidateExtraction(
        extraction_id="x1",
        source_text="The intervention caused a reduction in pain.",
        passage_reference="Methods",
        candidate_cause="intervention",
        candidate_effect="reduction",
        relationship_type=RelationshipType.CAUSAL,
        supporting_text="The intervention caused a reduction in pain.",
        confidence=0.9,
        notes="explicitly causal",
    )

    resolver = InMemoryOntologyResolver(
        {
            "intervention": Variable(
                variable_id="v1",
                label="intervention",
                concept=Concept(concept_id="c1", label="Intervention"),
            ),
            "reduction": Variable(
                variable_id="v2",
                label="reduction",
                concept=Concept(concept_id="c2", label="Reduction"),
            ),
        }
    )
    translation = translate_candidate_extraction(extraction, source_id="s1", source_title="Study 1", resolver=resolver)

    assert isinstance(translation.source, type(translation.source))
    assert translation.source.source_id == "s1"
    assert translation.evidence.source is translation.source
    assert isinstance(translation.proposed_claim, ProposedCausalClaim)
    assert translation.proposed_claim.cause.label == "intervention"
    assert translation.proposed_claim.effect.label == "reduction"
    assert translation.proposed_claim.evidence[0] is translation.evidence
    assert "candidate ProposedCausalClaim" in translation.notes


def test_associational_extraction_does_not_produce_proposed_causal_claim():
    extraction = CandidateExtraction(
        extraction_id="x2",
        source_text="Pain was associated with decreased mobility.",
        passage_reference="Results",
        candidate_cause="pain",
        candidate_effect="decreased mobility",
        relationship_type=RelationshipType.ASSOCIATIONAL,
        supporting_text="Pain was associated with decreased mobility.",
        confidence=0.7,
        notes="associational",
    )

    resolver = InMemoryOntologyResolver({})
    translation = translate_candidate_extraction(extraction, source_id="s2", source_title="Study 2", resolver=resolver)

    assert translation.proposed_claim is None
    assert "not explicitly causal" in translation.notes


def test_uncertain_extraction_does_not_produce_proposed_causal_claim():
    extraction = CandidateExtraction(
        extraction_id="x3",
        source_text="The relationship between treatment and outcome was unclear.",
        passage_reference="Discussion",
        candidate_cause="treatment",
        candidate_effect="outcome",
        relationship_type=RelationshipType.UNCERTAIN,
        supporting_text="The relationship between treatment and outcome was unclear.",
        confidence=0.5,
        notes="uncertain",
    )

    resolver = InMemoryOntologyResolver({})
    translation = translate_candidate_extraction(extraction, source_id="s3", source_title="Study 3", resolver=resolver)

    assert translation.proposed_claim is None
    assert translation.evidence.source.title == "Study 3"
    assert translation.evidence.description == extraction.supporting_text
    assert "not explicitly causal" in translation.notes


def test_translation_does_not_create_curation_decision():
    extraction = CandidateExtraction(
        extraction_id="x4",
        source_text="The intervention caused a reduction in pain.",
        passage_reference="Conclusion",
        candidate_cause="intervention",
        candidate_effect="reduction",
        relationship_type=RelationshipType.CAUSAL,
        supporting_text="The intervention caused a reduction in pain.",
        confidence=0.9,
        notes="explicitly causal",
    )

    resolver = InMemoryOntologyResolver(
        {
            "intervention": Variable(
                variable_id="v5",
                label="intervention",
                concept=Concept(concept_id="c5", label="Intervention"),
            ),
            "reduction": Variable(
                variable_id="v6",
                label="reduction",
                concept=Concept(concept_id="c6", label="Reduction"),
            ),
        }
    )
    translation = translate_candidate_extraction(extraction, source_id="s4", source_title="Study 4", resolver=resolver)

    assert translation.proposed_claim is not None
    assert not hasattr(translation, "curation_decision")
    assert translation.proposed_claim.evidence[0].source is translation.source


def test_causal_extraction_with_unresolved_cause_does_not_produce_proposed_causal_claim():
    extraction = CandidateExtraction(
        extraction_id="x5",
        source_text="The intervention caused a reduction in pain.",
        passage_reference="Abstract",
        candidate_cause="intervention",
        candidate_effect="reduction",
        relationship_type=RelationshipType.CAUSAL,
        supporting_text="The intervention caused a reduction in pain.",
        confidence=0.9,
        notes="explicitly causal",
    )

    resolver = InMemoryOntologyResolver(
        {
            "reduction": Variable(
                variable_id="v7",
                label="reduction",
                concept=Concept(concept_id="c7", label="Reduction"),
            )
        }
    )
    translation = translate_candidate_extraction(extraction, source_id="s5", source_title="Study 5", resolver=resolver)

    assert translation.proposed_claim is None
    assert translation.cause_resolution.extracted_term == "intervention"
    assert translation.cause_resolution.resolved_variable is None
    assert translation.effect_resolution.is_resolved is True
    assert "remain unresolved" in translation.notes


def test_causal_extraction_with_unresolved_effect_does_not_produce_proposed_causal_claim():
    extraction = CandidateExtraction(
        extraction_id="x6",
        source_text="The intervention caused a reduction in pain.",
        passage_reference="Abstract",
        candidate_cause="intervention",
        candidate_effect="reduction",
        relationship_type=RelationshipType.CAUSAL,
        supporting_text="The intervention caused a reduction in pain.",
        confidence=0.9,
        notes="explicitly causal",
    )

    resolver = InMemoryOntologyResolver(
        {
            "intervention": Variable(
                variable_id="v8",
                label="intervention",
                concept=Concept(concept_id="c8", label="Intervention"),
            )
        }
    )
    translation = translate_candidate_extraction(extraction, source_id="s6", source_title="Study 6", resolver=resolver)

    assert translation.proposed_claim is None
    assert translation.effect_resolution.extracted_term == "reduction"
    assert translation.effect_resolution.resolved_variable is None
    assert "remain unresolved" in translation.notes


def test_causal_extraction_with_neither_endpoint_resolved_does_not_produce_proposed_causal_claim():
    extraction = CandidateExtraction(
        extraction_id="x7",
        source_text="The intervention caused a reduction in pain.",
        passage_reference="Abstract",
        candidate_cause="intervention",
        candidate_effect="reduction",
        relationship_type=RelationshipType.CAUSAL,
        supporting_text="The intervention caused a reduction in pain.",
        confidence=0.9,
        notes="explicitly causal",
    )

    resolver = InMemoryOntologyResolver({})
    translation = translate_candidate_extraction(extraction, source_id="s7", source_title="Study 7", resolver=resolver)

    assert translation.proposed_claim is None
    assert translation.cause_resolution.resolved_variable is None
    assert translation.effect_resolution.resolved_variable is None
    assert translation.cause_resolution.extracted_term == "intervention"
    assert translation.effect_resolution.extracted_term == "reduction"
    assert "remain unresolved" in translation.notes
