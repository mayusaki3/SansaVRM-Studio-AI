"""
SansaVRM Studio AI
Local Server PoC

This module provides a minimal local FastAPI server for
architecture validation UI and project workspace APIs.
"""

from dataclasses import asdict
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from src.python.governance_evaluator import (
    GovernanceRule,
    GovernanceTarget,
)
from src.python.project_persistence import (
    PersistenceError,
    export_project_package,
    save_project,
    validate_project_import,
)
from src.python.project_workspace import (
    Artifact,
    ProjectWorkspace,
    ValidationError,
    WorkflowRun,
    WorkflowStep,
)
from src.python.workflow_engine import WorkflowEngine


class SaveProjectRequest(BaseModel):
    root_path: str


class ExportProjectRequest(BaseModel):
    root_path: str
    output_zip_path: str


class ValidateProjectRequest(BaseModel):
    root_path: str


app = FastAPI()

workspace = ProjectWorkspace(
    project_id="prj-demo",
    project_name="demo_project",
    schema_version="0.1.0",
    local_only_default=True,
)

engine = WorkflowEngine(workspace)

governance_diagnostics: list[dict] = []

component_registry = [
    {
        "component_id": "body-001",
        "component_type": "body",
        "source_sansavrm": "SansaVRM_A",
        "assembly_allowed": True,
        "reason": "allowed",
    },
    {
        "component_id": "hair-001",
        "component_type": "hair",
        "source_sansavrm": "SansaVRM_B",
        "assembly_allowed": False,
        "reason": "assembly_denied_by_policy",
    },
    {
        "component_id": "clothing-001",
        "component_type": "clothing",
        "source_sansavrm": "SansaVRM_C",
        "assembly_allowed": True,
        "reason": "allowed",
    },
]


def ensure_source_artifact() -> None:
    if "artifact-source-image-001" in workspace.artifacts:
        return

    workspace.register_artifact(
        Artifact(
            artifact_id="artifact-source-image-001",
            artifact_type="source_image",
            path="artifacts/source/source_001.png",
        )
    )


def run_demo_workflow(
    run_index: int | None = None,
    deny_decomposition: bool = False,
) -> WorkflowRun:
    """Execute deterministic demo workflow."""

    ensure_source_artifact()

    if run_index is None:
        run_index = len(workspace.workflow_runs) + 1

    run_suffix = f"{run_index:03d}"

    workflow_run = WorkflowRun(
        workflow_run_id=f"run-demo-{run_suffix}",
        workflow_type="ai_preprocess",
        status="running",
        local_only=True,
    )

    risk_step = WorkflowStep(
        step_id=f"step-risk-{run_suffix}",
        step_type="copyright_risk_assessment",
        status="pending",
        input_artifacts=["artifact-source-image-001"],
    )

    risk_artifact = Artifact(
        artifact_id=f"artifact-risk-result-{run_suffix}",
        artifact_type="copyright_risk_result",
        path=f"artifacts/risk/risk_{run_suffix}.json",
    )

    engine.execute_step(
        workflow_run,
        risk_step,
        risk_artifact,
    )

    decomposition_step = WorkflowStep(
        step_id=f"step-decomposition-{run_suffix}",
        step_type="decomposition",
        status="pending",
        input_artifacts=["artifact-source-image-001"],
    )

    decomposition_artifact = Artifact(
        artifact_id=f"artifact-decomposition-{run_suffix}",
        artifact_type="decomposition_result",
        path=f"artifacts/decomposition/decomposition_{run_suffix}.json",
    )

    governance_target = GovernanceTarget(
        target_id="artifact-source-image-001",
        target_type="asset",
        rules=[],
    )

    if deny_decomposition:
        governance_target.rules.append(
            GovernanceRule(
                operation="decompose",
                allowed=False,
                reason="decomposition_denied_by_policy",
            )
        )

    try:
        engine.execute_step(
            workflow_run,
            decomposition_step,
            decomposition_artifact,
            governance_operation="decompose",
            governance_target=governance_target,
        )
    except ValidationError as exc:
        workflow_run.status = "failed"

        governance_diagnostics.append(
            {
                "workflow_run_id": workflow_run.workflow_run_id,
                "step_id": decomposition_step.step_id,
                "operation": "decompose",
                "allowed": False,
                "reason": str(exc),
            }
        )

        workspace.register_workflow_run(workflow_run)

        return workflow_run

    workflow_run.status = "completed"
    workspace.register_workflow_run(workflow_run)

    return workflow_run


def seed_demo_data() -> None:
    if workspace.artifacts or workspace.workflow_runs:
        return

    run_demo_workflow(run_index=1)


seed_demo_data()


@app.get("/")
def index():
    index_path = Path("web") / "index.html"

    if not index_path.exists():
        raise HTTPException(
            status_code=404,
            detail="web/index.html not found",
        )

    return FileResponse(index_path)


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/project")
def project_summary():
    return {
        "project_id": workspace.project_id,
        "project_name": workspace.project_name,
        "schema_version": workspace.schema_version,
        "artifact_count": len(workspace.artifacts),
        "workflow_run_count": len(workspace.workflow_runs),
    }


@app.get("/api/components")
def components():
    return {
        "components": component_registry,
    }


@app.get("/api/artifacts")
def artifacts():
    return {
        "artifacts": [asdict(a) for a in workspace.artifacts.values()]
    }


@app.get("/api/workflow-runs")
def workflow_runs():
    return {
        "workflow_runs": [asdict(r) for r in workspace.workflow_runs.values()]
    }


@app.get("/api/workflow-graph")
def workflow_graph():
    return {
        "dependency_graph": {
            k: asdict(v)
            for k, v in engine.dependency_graph.items()
        }
    }


@app.get("/api/governance-diagnostics")
def governance_diagnostics_endpoint():
    return {
        "diagnostics": governance_diagnostics,
    }


@app.post("/api/workflows/demo/run")
def run_demo_workflow_endpoint(
    deny_decomposition: bool = False,
):
    workflow_run = run_demo_workflow(
        deny_decomposition=deny_decomposition,
    )

    return {
        "status": workflow_run.status,
        "workflow_run": asdict(workflow_run),
    }


@app.post("/api/project/save")
def save_current_project(request: SaveProjectRequest):
    save_project(workspace, request.root_path)

    return {
        "status": "saved",
        "root_path": request.root_path,
    }


@app.post("/api/project/export")
def export_current_project(request: ExportProjectRequest):
    save_project(workspace, request.root_path)
    export_project_package(
        request.root_path,
        request.output_zip_path,
    )

    return {
        "status": "exported",
        "output_zip_path": request.output_zip_path,
    }


@app.post("/api/project/validate-import")
def validate_imported_project(request: ValidateProjectRequest):
    try:
        validate_project_import(request.root_path)
    except PersistenceError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    return {
        "status": "valid",
        "root_path": request.root_path,
    }
