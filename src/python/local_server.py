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

from src.python.project_persistence import (
    PersistenceError,
    export_project_package,
    save_project,
    validate_project_import,
)
from src.python.project_workspace import (
    ProjectWorkspace,
)
from src.python.workflow_engine import WorkflowEngine


class SaveProjectRequest(BaseModel):
    """Request body for saving project workspace."""

    root_path: str


class ExportProjectRequest(BaseModel):
    """Request body for exporting project package."""

    root_path: str
    output_zip_path: str


class ValidateProjectRequest(BaseModel):
    """Request body for validating imported project."""

    root_path: str


app = FastAPI()

workspace = ProjectWorkspace(
    project_id="prj-demo",
    project_name="demo_project",
    schema_version="0.1.0",
    local_only_default=True,
)

engine = WorkflowEngine(workspace)


@app.get("/")
def index():
    """Serve minimal validation UI."""

    index_path = Path("web") / "index.html"

    if not index_path.exists():
        raise HTTPException(
            status_code=404,
            detail="web/index.html not found",
        )

    return FileResponse(index_path)


@app.get("/api/health")
def health():
    """Health check endpoint."""

    return {
        "status": "ok"
    }


@app.get("/api/project")
def project_summary():
    """Project summary endpoint."""

    return {
        "project_id": workspace.project_id,
        "project_name": workspace.project_name,
        "schema_version": workspace.schema_version,
        "artifact_count": len(workspace.artifacts),
        "workflow_run_count": len(
            workspace.workflow_runs
        ),
    }


@app.get("/api/artifacts")
def artifacts():
    """Artifact registry endpoint."""

    return {
        "artifacts": [
            asdict(a)
            for a in workspace.artifacts.values()
        ]
    }


@app.get("/api/workflow-runs")
def workflow_runs():
    """Workflow run endpoint."""

    return {
        "workflow_runs": [
            asdict(r)
            for r in workspace.workflow_runs.values()
        ]
    }


@app.get("/api/workflow-graph")
def workflow_graph():
    """Workflow dependency graph endpoint."""

    return {
        "dependency_graph": {
            k: asdict(v)
            for k, v in engine.dependency_graph.items()
        }
    }


@app.post("/api/project/save")
def save_current_project(request: SaveProjectRequest):
    """Save current project workspace."""

    save_project(workspace, request.root_path)

    return {
        "status": "saved",
        "root_path": request.root_path,
    }


@app.post("/api/project/export")
def export_current_project(request: ExportProjectRequest):
    """Export current project package."""

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
    """Validate imported project path."""

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
