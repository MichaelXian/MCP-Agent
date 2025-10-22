from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Addition")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together"""
    return a + b

# Run the server
if __name__ == "__main__":
    mcp.run()