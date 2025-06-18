from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from .create_event import create_event
from .list_dashboards import list_dashboards
from .list_monitors import list_monitors
from .search_logs import search_logs


def register_tools(mcp: FastMCP) -> None:
    """Register all Datadog tools on the given MCP instance."""
    mcp.add_tool(list_dashboards)
    mcp.add_tool(list_monitors)
    mcp.add_tool(create_event)
    mcp.add_tool(search_logs)


__all__ = [
    "register_tools",
    "list_dashboards",
    "list_monitors",
    "create_event",
    "search_logs",
]
