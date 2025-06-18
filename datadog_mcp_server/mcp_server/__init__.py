from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from .configure_datadog import configure_datadog
from .create_event import create_event
from .create_context import create_context
from .delete_context import delete_context
from .get_context import get_context
from .health_check import health_check
from .list_contexts import list_contexts
from .list_dashboards import list_dashboards
from .list_monitors import list_monitors
from .query_model import query_model
from .search_logs import search_logs
from .update_context import update_context


def register_tools(mcp: FastMCP) -> None:
    """Register all Datadog tools on the given MCP instance."""
    mcp.add_tool(configure_datadog)
    mcp.add_tool(create_context)
    mcp.add_tool(get_context)
    mcp.add_tool(update_context)
    mcp.add_tool(delete_context)
    mcp.add_tool(list_contexts)
    mcp.add_tool(query_model)
    mcp.add_tool(list_dashboards)
    mcp.add_tool(list_monitors)
    mcp.add_tool(create_event)
    mcp.add_tool(search_logs)


__all__ = [
    "register_tools",
    "configure_datadog",
    "create_context",
    "get_context",
    "update_context",
    "delete_context",
    "list_contexts",
    "query_model",
    "list_dashboards",
    "list_monitors",
    "create_event",
    "search_logs",
]
