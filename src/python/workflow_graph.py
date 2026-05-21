"""
SansaVRM Studio AI
Workflow Graph PoC

This module provides an executable semantic graph model for
workflow, artifact, governance, provenance, and diagnostics tracking.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorkflowGraphNode:
    """Workflow graph node.

    Args:
        node_id: Unique node identifier.
        node_type: Node type, such as workflow, step, artifact,
            governance, provenance, or diagnostics.
        state: Lifecycle state, such as pending, ready, running,
            completed, failed, or blocked.
        metadata: Additional node metadata.
    """

    node_id: str
    node_type: str
    state: str = "pending"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkflowGraphEdge:
    """Workflow graph edge.

    Args:
        edge_id: Unique edge identifier.
        edge_type: Edge type, such as input, output,
            derived_from, governed_by, reviewed_by, or diagnostic_for.
        source_node_id: Source node identifier.
        target_node_id: Target node identifier.
        metadata: Additional edge metadata.
    """

    edge_id: str
    edge_type: str
    source_node_id: str
    target_node_id: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkflowGraph:
    """Executable semantic workflow graph.

    The graph is intended to be the authority for workflow execution,
    provenance tracing, governance propagation, diagnostics tracing,
    and workspace reconstruction.
    """

    graph_id: str
    nodes: dict[str, WorkflowGraphNode] = field(default_factory=dict)
    edges: dict[str, WorkflowGraphEdge] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def add_node(self, node: WorkflowGraphNode) -> None:
        """Add or replace a graph node."""

        self.nodes[node.node_id] = node

    def add_edge(self, edge: WorkflowGraphEdge) -> None:
        """Add or replace a graph edge.

        Raises:
            ValueError: If the source or target node does not exist.
        """

        if edge.source_node_id not in self.nodes:
            raise ValueError(
                f"Missing source node: {edge.source_node_id}"
            )

        if edge.target_node_id not in self.nodes:
            raise ValueError(
                f"Missing target node: {edge.target_node_id}"
            )

        self.edges[edge.edge_id] = edge

    def update_node_state(
        self,
        node_id: str,
        state: str,
    ) -> None:
        """Update node lifecycle state."""

        if node_id not in self.nodes:
            raise ValueError(f"Missing node: {node_id}")

        self.nodes[node_id].state = state

    def find_outgoing_edges(
        self,
        node_id: str,
        edge_type: str | None = None,
    ) -> list[WorkflowGraphEdge]:
        """Find outgoing edges from a node."""

        return [
            edge
            for edge in self.edges.values()
            if edge.source_node_id == node_id
            and (
                edge_type is None
                or edge.edge_type == edge_type
            )
        ]

    def find_incoming_edges(
        self,
        node_id: str,
        edge_type: str | None = None,
    ) -> list[WorkflowGraphEdge]:
        """Find incoming edges to a node."""

        return [
            edge
            for edge in self.edges.values()
            if edge.target_node_id == node_id
            and (
                edge_type is None
                or edge.edge_type == edge_type
            )
        ]

    def find_derived_artifacts(
        self,
        source_node_id: str,
    ) -> list[WorkflowGraphNode]:
        """Find artifact nodes derived from source node."""

        edges = self.find_outgoing_edges(
            source_node_id,
            edge_type="derived_from",
        )

        return [
            self.nodes[edge.target_node_id]
            for edge in edges
            if self.nodes[edge.target_node_id].node_type == "artifact"
        ]

    def find_restriction_sources(
        self,
        node_id: str,
    ) -> list[WorkflowGraphNode]:
        """Find governance nodes that govern the specified node."""

        edges = self.find_incoming_edges(
            node_id,
            edge_type="governed_by",
        )

        return [
            self.nodes[edge.source_node_id]
            for edge in edges
            if self.nodes[edge.source_node_id].node_type == "governance"
        ]

    def find_diagnostics_for_node(
        self,
        node_id: str,
    ) -> list[WorkflowGraphNode]:
        """Find diagnostics nodes for the specified node."""

        edges = self.find_incoming_edges(
            node_id,
            edge_type="diagnostic_for",
        )

        return [
            self.nodes[edge.source_node_id]
            for edge in edges
            if self.nodes[edge.source_node_id].node_type == "diagnostics"
        ]

    def find_blocked_nodes(self) -> list[WorkflowGraphNode]:
        """Find blocked nodes."""

        return [
            node
            for node in self.nodes.values()
            if node.state == "blocked"
        ]

    def to_dict(self) -> dict[str, Any]:
        """Serialize graph to dict."""

        return {
            "graph_id": self.graph_id,
            "metadata": self.metadata,
            "nodes": {
                node_id: {
                    "node_id": node.node_id,
                    "node_type": node.node_type,
                    "state": node.state,
                    "metadata": node.metadata,
                }
                for node_id, node in self.nodes.items()
            },
            "edges": {
                edge_id: {
                    "edge_id": edge.edge_id,
                    "edge_type": edge.edge_type,
                    "source_node_id": edge.source_node_id,
                    "target_node_id": edge.target_node_id,
                    "metadata": edge.metadata,
                }
                for edge_id, edge in self.edges.items()
            },
        }
