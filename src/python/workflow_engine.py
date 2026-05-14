"""
SansaVRM Studio AI
Workflow Engine PoC
"""

from dataclasses import dataclass, field
from typing import Dict, List

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

    def execute_step(
        self,
        workflow_run: WorkflowRun,
        step: WorkflowStep,
        output_artifact: Artifact,
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
    ) -> None:
        """
        Rerun workflow step.
        """

        self.execute_step(
            workflow_run,
            new_step,
            output_artifact,
        )
