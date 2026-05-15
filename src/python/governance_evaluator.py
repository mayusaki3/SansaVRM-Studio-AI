"""
SansaVRM Studio AI
Governance Evaluation PoC

This module provides a minimal governance evaluation layer.

IMPORTANT:
- This is a temporary PoC implementation.
- SansaVRM governance schema is the future authority.
- Studio AI must behave as a governance consumer.
"""

from dataclasses import dataclass, field


@dataclass
class GovernanceRule:
    """Simple governance rule."""

    operation: str
    allowed: bool
    reason: str


@dataclass
class GovernanceTarget:
    """Target object for governance evaluation."""

    target_id: str
    target_type: str
    rules: list[GovernanceRule] = field(default_factory=list)


@dataclass
class GovernanceEvaluationResult:
    """Governance evaluation result."""

    operation: str
    allowed: bool
    reason: str
    target_id: str


class GovernanceEvaluator:
    """
    Governance evaluator.

    This evaluator is intentionally simple.
    Future versions should consume SansaVRM governance schema.
    """

    def evaluate(
        self,
        operation: str,
        target: GovernanceTarget,
    ) -> GovernanceEvaluationResult:
        """
        Evaluate operation against governance rules.

        Args:
            operation: Requested operation.
            target: Governance target.

        Returns:
            Governance evaluation result.
        """

        for rule in target.rules:
            if rule.operation != operation:
                continue

            return GovernanceEvaluationResult(
                operation=operation,
                allowed=rule.allowed,
                reason=rule.reason,
                target_id=target.target_id,
            )

        return GovernanceEvaluationResult(
            operation=operation,
            allowed=True,
            reason="no_rule_defined",
            target_id=target.target_id,
        )

    def can_decompose(
        self,
        target: GovernanceTarget,
    ) -> GovernanceEvaluationResult:
        """Evaluate decomposition permission."""

        return self.evaluate(
            operation="decompose",
            target=target,
        )

    def can_extract_component(
        self,
        target: GovernanceTarget,
    ) -> GovernanceEvaluationResult:
        """Evaluate component extraction permission."""

        return self.evaluate(
            operation="extract_component",
            target=target,
        )

    def can_assemble(
        self,
        target: GovernanceTarget,
    ) -> GovernanceEvaluationResult:
        """Evaluate assembly permission."""

        return self.evaluate(
            operation="assemble",
            target=target,
        )

    def can_convert(
        self,
        target: GovernanceTarget,
    ) -> GovernanceEvaluationResult:
        """Evaluate conversion permission."""

        return self.evaluate(
            operation="convert",
            target=target,
        )
