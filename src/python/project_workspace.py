"""
SansaVRM Studio AI
Project Workspace PoC

This module provides a minimal project workspace implementation.
"""

from dataclasses import dataclass, field
from typing import Dict, List

VALID_STATUS = {
    "pending",
    "running",
    "completed",
    "failed",
    "skipped",
    "cancelled",
}


class ValidationError(Exception):
    """Raised when schema validation fails."""


@dataclass
class Artifact:
    """Artifact metadata."""

    artifact_id: str
    artifact_type: str
    path: str


@dataclass
class WorkflowStep:
    """Workflow step metadata."""

    step_id: str
    step_type: str
    status: str
    input_artifacts: List[str] = field(default_factory=list)
    output_artifacts: List[str] = field(default_factory=list)

    def validate(self) -> None:
        """Validate workflow step."""

        if self.status not in VALID_STATUS:
            raise ValidationError(
                f"Invalid status: {self.status}"
            )


@dataclass
class WorkflowRun:
    """Workflow run metadata."""

    workflow_run_id: str
    workflow_type: str
    status: str
    local_only: bool
    steps: List[WorkflowStep] = field(default_factory=list)

    def validate(self) -> None:
        """Validate workflow run."""

        if self.status not in VALID_STATUS:
            raise ValidationError(
                f"Invalid status: {self.status}"
            )

        for step in self.steps:
            step.validate()


@dataclass
class ProjectWorkspace:
    """Project workspace metadata."""

    project_id: str
    project_name: str
    schema_version: str
    local_only_default: bool
    artifacts: Dict[str, Artifact] = field(default_factory=dict)
    workflow_runs: Dict[str, WorkflowRun] = field(default_factory=dict)

    def register_artifact(self, artifact: Artifact) -> None:
        """Register artifact."""

        self.artifacts[artifact.artifact_id] = artifact

    def register_workflow_run(
        self,
        workflow_run: WorkflowRun,
    ) -> None:
        """Register workflow run."""

        workflow_run.validate()

        self.workflow_runs[
            workflow_run.workflow_run_id
        ] = workflow_run
