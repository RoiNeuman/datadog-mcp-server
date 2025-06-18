from enum import StrEnum
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="datadog_mcp_server",
    description="Datadog MCP Server",
)


class Transport(StrEnum):
    """Transport type for the MCP server."""
    stdio = "stdio"
    sse = "sse"


if __name__ == "__main__":
    transport = Transport.stdio
    if transport is Transport.stdio:
        print("Running MCP server with stdio transport")
    elif transport is Transport.sse:
        print("Running MCP server with SSE transport")
    else:
        raise ValueError(f"Unsupported transport: {transport}")
    # Run the MCP server with the specified transport
    mcp.run(transport=transport.value)
