"""Datadog MCP server package."""

from .mcp_server import (
    create_event,
    list_dashboards,
    list_monitors,
    register_tools,
    search_logs,
)

__all__ = [
    "register_tools",
    "list_dashboards",
    "list_monitors",
    "create_event",
    "search_logs",
]
