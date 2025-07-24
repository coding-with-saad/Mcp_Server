# server.py
from mcp.server.fastmcp import FastMCP
import webbrowser
import urllib.parse

# Create an MCP server
mcp = FastMCP("Google search")

# Add an addition tool
@mcp.tool()
def open_google_search(query):
    """Search in google with query"""
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}"
    webbrowser.open(url)

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
