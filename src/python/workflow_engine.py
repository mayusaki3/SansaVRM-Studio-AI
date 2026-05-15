"""
SansaVRM Studio AI
Workflow Engine PoC
"""

from dataclasses import dataclass, field
from typing import Dict, List

from src.python.governance_evaluator import (
    GovernanceEvaluationResult,
    GovernanceEvaluator,
    GovernanceTarget,
)
from src.python.project_workspace import (
    Artifact,
    ProjectWorkspace,
    ValidationError,
    WorkflowRun,
    WorkflowStep,
)


@dataclass
class ArtifactDependency:
    """Artifact dependency graph entry."""

    artifact_id: str
    created_by_step: str
    depends_on: List[str] = field(default_factory=list)


class WorkflowEngine:
    """Minimal workflow engine."""

    def __init__(
        self,
        workspace: ProjectWorkspace,
    ) -> None:
        self.workspace = workspace
        self.dependency_graph: Dict[
            str,
            ArtifactDependency,
        ] = {}

        self.governance_evaluator = GovernanceEvaluator()

    def evaluate_governance(
        self,
        operation: str,
        governance_target: GovernanceTarget | None,
    ) -> GovernanceEvaluationResult | None:
        """
        Evaluate governance before workflow execution.

        Args:
            operation: Requested operation.
            governance_target: Governance target.

        Returns:
            Governance evaluation result or None.
        """

        if governance_target is None:
            return None

        return self.governance_evaluator.evaluate(
            operation=operation,
            target=governance_target,
        )

    def execute_step(
        self,
        workflow_run: WorkflowRun,
        step: WorkflowStep,
        output_artifact: Artifact,
        governance_operation: str | None = None,
        governance_target: GovernanceTarget | None = None,
    ) -> None:
        """
        Execute workflow step.
        """

        for artifact_id in step.input_artifacts:
            if artifact_id not in self.workspace.artifacts:
                step.status = "failed"
                raise ValidationError(
                    f"Missing input artifact: {artifact_id}"
                )

        governance_result = self.evaluate_governance(
            operation=(
                governance_operation
                or step.step_type
            ),
            governance_target=governance_target,
        )

        if governance_result is not None:
            if governance_result.allowed is False:
                step.status = "failed"

                workflow_run.steps.append(step)

                raise ValidationError(
                    "Governance denied operation: "
                    f"{governance_result.operation} / "
                    f"reason={governance_result.reason}"
                )

        step.status = "running"

        self.workspace.register_artifact(
            output_artifact
        )

        self.dependency_graph[
            output_artifact.artifact_id
        ] = ArtifactDependency(
            artifact_id=output_artifact.artifact_id,
            created_by_step=step.step_id,
            depends_on=step.input_artifacts,
        )

        step.output_artifacts.append(
            output_artifact.artifact_id
        )

        step.status = "completed"

        workflow_run.steps.append(step)

    def rerun_step(
        self,
        workflow_run: WorkflowRun,
        original_step: WorkflowStep,
        new_step: WorkflowStep,
        output_artifact: Artifact,
        governance_operation: str | None = None,
        governance_target: GovernanceTarget | None = None,
    ) -> None:
        """
        Rerun workflow step.
        """

        self.execute_step(
            workflow_run,
            new_step,
            output_artifact,
            governance_operation=governance_operation,
            governance_target=governance_target,
        )
