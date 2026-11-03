"\""
Scrapling MCP Server Module.
Provides web scraping capabilities via the Model Context Protocol (MCP).
"\""

from typing import Optional
from mcp.server.fastmcp import FastMCP
from scrapling import Fetcher

mcp = FastMCP("Scrapling Tools")

@mcp.tool()
def extract_website_text(url: str) -> str:
    "\""
    Accesses a website and extracts its content as clean text.
    "\""
    if not url:
        return "Error: URL parameter cannot be empty."

    try:
        fetcher = Fetcher()
        page = fetcher.get(url)
        
        if not page:
            return f"Error: Received empty response from {url}"
            
        return page.text
    except Exception as e:
        return f"Failed to access or parse the page. Error details: {str(e)}"

if __name__ == "__main__":
    mcp.run()
