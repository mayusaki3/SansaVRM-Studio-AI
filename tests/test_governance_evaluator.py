"""Governance evaluator tests."""

from src.python.governance_evaluator import (
    GovernanceEvaluator,
    GovernanceRule,
    GovernanceTarget,
)


def test_decompose_denied() -> None:
    """GOV-001: decomposition denied."""

    evaluator = GovernanceEvaluator()

    target = GovernanceTarget(
        target_id="asset-001",
        target_type="asset",
        rules=[
            GovernanceRule(
                operation="decompose",
                allowed=False,
                reason="decomposition_denied",
            )
        ],
    )

    result = evaluator.can_decompose(target)

    assert result.allowed is False
    assert result.reason == "decomposition_denied"


def test_assembly_denied() -> None:
    """GOV-002: assembly denied."""

    evaluator = GovernanceEvaluator()

    target = GovernanceTarget(
        target_id="component-001",
        target_type="component",
        rules=[
            GovernanceRule(
                operation="assemble",
                allowed=False,
                reason="assembly_denied",
            )
        ],
    )

    result = evaluator.can_assemble(target)

    assert result.allowed is False
    assert result.reason == "assembly_denied"


def test_conversion_denied() -> None:
    """GOV-003: conversion denied."""

    evaluator = GovernanceEvaluator()

    target = GovernanceTarget(
        target_id="asset-002",
        target_type="asset",
        rules=[
            GovernanceRule(
                operation="convert",
                allowed=False,
                reason="conversion_denied",
            )
        ],
    )

    result = evaluator.can_convert(target)

    assert result.allowed is False
    assert result.reason == "conversion_denied"


def test_default_allow_when_no_rule() -> None:
    """No rule defaults to allow."""

    evaluator = GovernanceEvaluator()

    target = GovernanceTarget(
        target_id="asset-003",
        target_type="asset",
    )

    result = evaluator.can_convert(target)

    assert result.allowed is True
    assert result.reason == "no_rule_defined"
