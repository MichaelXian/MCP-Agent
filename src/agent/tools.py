from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
async def add(a: float, b: float) -> float:
    """Add two numbers together"""
    print("Using MCP tool add")
    return a + b