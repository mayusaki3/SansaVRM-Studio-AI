"""Assembly API models."""

from pydantic import BaseModel


class ComponentSelectionRequest(BaseModel):
    """Component selection request."""

    slot_name: str
    component_id: str


class AssemblyPreviewResponse(BaseModel):
    """Assembly preview response."""

    selected_components: dict
    provenance_graph: dict
    conflicts: list
