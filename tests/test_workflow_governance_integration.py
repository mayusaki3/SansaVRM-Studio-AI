"""Workflow governance integration tests."""

import pytest

from src.python.governance_evaluator import (
    GovernanceRule,
    GovernanceTarget,
)
from src.python.project_workspace import (
    Artifact,
    ProjectWorkspace,
    ValidationError,
    WorkflowRun,
    WorkflowStep,
)
from src.python.workflow_engine import WorkflowEngine


@pytest.fixture
def workspace() -> ProjectWorkspace:
    """Create test workspace."""

    workspace = ProjectWorkspace(
        project_id="prj-test",
        project_name="test_project",
        schema_version="0.1.0",
        local_only_default=True,
    )

    workspace.register_artifact(
        Artifact(
            artifact_id="artifact-source-001",
            artifact_type="source_image",
            path="source.png",
        )
    )

    return workspace


def test_governance_denied_step(
    workspace: ProjectWorkspace,
) -> None:
    """GOV-WF-001: denied workflow step."""

    engine = WorkflowEngine(workspace)

    workflow_run = WorkflowRun(
        workflow_run_id="run-001",
        workflow_type="assembly",
        status="running",
        local_only=True,
    )

    step = WorkflowStep(
        step_id="step-001",
        step_type="assemble",
        status="pending",
        input_artifacts=[
            "artifact-source-001",
        ],
    )

    output_artifact = Artifact(
        artifact_id="artifact-output-001",
        artifact_type="assembled_asset",
        path="assembled.sansavrm",
    )

    governance_target = GovernanceTarget(
        target_id="component-hair-001",
        target_type="component",
        rules=[
            GovernanceRule(
                operation="assemble",
                allowed=False,
                reason="assembly_denied",
            )
        ],
    )

    with pytest.raises(ValidationError):
        engine.execute_step(
            workflow_run=workflow_run,
            step=step,
            output_artifact=output_artifact,
            governance_operation="assemble",
            governance_target=governance_target,
        )

    assert step.status == "failed"


def test_governance_allowed_step(
    workspace: ProjectWorkspace,
) -> None:
    """GOV-WF-002: allowed workflow step."""

    engine = WorkflowEngine(workspace)

    workflow_run = WorkflowRun(
        workflow_run_id="run-002",
        workflow_type="conversion",
        status="running",
        local_only=True,
    )

    step = WorkflowStep(
        step_id="step-002",
        step_type="convert",
        status="pending",
        input_artifacts=[
            "artifact-source-001",
        ],
    )

    output_artifact = Artifact(
        artifact_id="artifact-output-002",
        artifact_type="converted_asset",
        path="converted.glb",
    )

    governance_target = GovernanceTarget(
        target_id="asset-001",
        target_type="asset",
    )

    engine.execute_step(
        workflow_run=workflow_run,
        step=step,
        output_artifact=output_artifact,
        governance_operation="convert",
        governance_target=governance_target,
    )

    assert step.status == "completed"
