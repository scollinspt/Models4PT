import pytest

from models4pt.domain import (
    Concept,
    CurationDecision,
    Evidence,
    Measurement,
    ProposedCausalClaim,
    Source,
    Variable,
)


def test_concept_variable_measurement_distinct_types():
    concept = Concept(concept_id="c1", label="Pain")
    variable = Variable(variable_id="v1", label="Pain intensity", concept=concept)
    measurement = Measurement(measurement_id="m1", label="NPRS", variable=variable)

    assert isinstance(concept, Concept)
    assert isinstance(variable, Variable)
    assert isinstance(measurement, Measurement)
    assert variable.concept is concept
    assert measurement.variable is variable


def test_variable_references_exactly_one_concept():
    concept = Concept(concept_id="c2", label="Quadriceps strength")
    variable = Variable(variable_id="v2", label="Affected-limb quadriceps strength at 12 weeks", concept=concept)

    assert variable.concept is concept


def test_variable_has_no_intrinsic_causal_role_fields():
    variable = Variable(variable_id="v3", label="Pain intensity", concept=Concept(concept_id="c3", label="Pain"))
    assert not hasattr(variable, "exposure")
    assert not hasattr(variable, "outcome")
    assert not hasattr(variable, "mediator")
    assert not hasattr(variable, "confounder")
    assert not hasattr(variable, "collider")


def test_measurement_references_variable_without_observed_value():
    variable = Variable(variable_id="v4", label="Pain intensity", concept=Concept(concept_id="c4", label="Pain"))
    measurement = Measurement(measurement_id="m2", label="Numeric Pain Rating Scale", variable=variable)

    assert measurement.variable is variable
    assert not hasattr(measurement, "value")
    assert not hasattr(measurement, "observed_value")


def test_source_and_evidence_are_distinct():
    source = Source(source_id="s1", title="Pain study")
    evidence = Evidence(evidence_id="e1", description="NPRS reduced", source=source)

    assert isinstance(source, Source)
    assert isinstance(evidence, Evidence)
    assert evidence.source is source
    assert source is not evidence


def test_one_source_can_produce_multiple_evidence_items():
    source = Source(source_id="s2", title="Strength study")
    evidence1 = Evidence(evidence_id="e2", description="Peak torque increased", source=source)
    evidence2 = Evidence(evidence_id="e3", description="MVC improved", source=source)

    assert evidence1.source is source
    assert evidence2.source is source
    assert evidence1 is not evidence2


def test_evidence_can_exist_without_causal_claim():
    source = Source(source_id="s3", title="Observation report")
    evidence = Evidence(evidence_id="e4", description="Participants reported less pain", source=source)

    assert evidence.source is source
    assert evidence.description == "Participants reported less pain"


def test_same_evidence_can_reference_multiple_proposed_causal_claims():
    concept = Concept(concept_id="c5", label="Pain")
    variable_a = Variable(variable_id="v5", label="Pain intensity", concept=concept)
    variable_b = Variable(variable_id="v6", label="Activity limitation", concept=Concept(concept_id="c6", label="Activity"))
    evidence = Evidence(evidence_id="e5", description="NPRS decreased with intervention", source=Source(source_id="s4", title="RCT"))
    claim1 = ProposedCausalClaim(proposal_id="p1", cause=variable_a, effect=variable_b, evidence=[evidence])
    claim2 = ProposedCausalClaim(proposal_id="p2", cause=variable_a, effect=variable_b, evidence=[evidence])

    assert evidence in claim1.evidence
    assert evidence in claim2.evidence
    assert claim1 is not claim2


def test_proposed_causal_claim_relates_exactly_one_cause_to_one_effect():
    cause = Variable(variable_id="v7", label="Pain intensity", concept=Concept(concept_id="c7", label="Pain"))
    effect = Variable(variable_id="v8", label="Mobility", concept=Concept(concept_id="c8", label="Mobility"))
    claim = ProposedCausalClaim(proposal_id="p3", cause=cause, effect=effect)

    assert claim.cause is cause
    assert claim.effect is effect


def test_cause_and_effect_cannot_be_same_variable():
    variable = Variable(variable_id="v9", label="Pain intensity", concept=Concept(concept_id="c9", label="Pain"))

    with pytest.raises(ValueError):
        ProposedCausalClaim(proposal_id="p4", cause=variable, effect=variable)


def test_proposed_causal_claim_rejects_same_variable_id_for_distinct_instances():
    cause = Variable(variable_id="v10", label="Pain intensity", concept=Concept(concept_id="c10", label="Pain"))
    effect = Variable(variable_id="v10", label="Pain intensity duplicate", concept=Concept(concept_id="c10", label="Pain"))

    with pytest.raises(ValueError):
        ProposedCausalClaim(proposal_id="p8", cause=cause, effect=effect)


def test_proposed_causal_claim_contains_no_accepted_rejected_state():
    claim = ProposedCausalClaim(
        proposal_id="p5",
        cause=Variable(variable_id="v10", label="Pain intensity", concept=Concept(concept_id="c10", label="Pain")),
        effect=Variable(variable_id="v11", label="Function", concept=Concept(concept_id="c11", label="Function")),
    )

    assert not hasattr(claim, "accepted")
    assert not hasattr(claim, "rejected")


def test_curation_decision_is_separate_and_multiple_decisions_allowed():
    claim = ProposedCausalClaim(
        proposal_id="p6",
        cause=Variable(variable_id="v12", label="Pain intensity", concept=Concept(concept_id="c12", label="Pain")),
        effect=Variable(variable_id="v13", label="Quality of life", concept=Concept(concept_id="c13", label="Quality of life")),
    )
    decision1 = CurationDecision(decision_id="d1", proposal=claim, reviewer="Alice", rationale="Needs more evidence")
    decision2 = CurationDecision(decision_id="d2", proposal=claim, reviewer="Bob", rationale="Agree with direction")

    assert decision1.proposal is claim
    assert decision2.proposal is claim
    assert decision1 is not decision2
