from enum import StrEnum
from typing import Annotated

import typer
from mcp.server.fastmcp import FastMCP

from datadog_mcp_server.mcp_server import register_tools

mcp = FastMCP(
    name="datadog_mcp_server",
    description="Datadog MCP Server",
)
register_tools(mcp)


class Transport(StrEnum):
    """Transport type for the MCP server."""

    stdio = "stdio"
    sse = "sse"


def _run_server(transport: Annotated[Transport, typer.Option(help="MCP transport")]) -> None:
    """Run the MCP server using the selected transport."""
    if transport is Transport.stdio:
        print("Running MCP server with stdio transport")
    elif transport is Transport.sse:
        print("Running MCP server with SSE transport")
    else:
        raise ValueError(f"Unsupported transport: {transport}")
    mcp.run(transport=transport.value)


def cli() -> None:
    """Entry point for the ``datadog_mcp_server`` console script."""

    typer.run(_run_server)


if __name__ == "__main__":
    cli()
