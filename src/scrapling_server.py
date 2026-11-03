"""
Scrapling MCP Server Module.

Provides web scraping capabilities via the Model Context Protocol (MCP).
"""

from typing import Optional
from mcp.server.fastmcp import FastMCP
from scrapling import Fetcher

# Initialize the MCP server
mcp = FastMCP("Scrapling Tools")

@mcp.tool()
def extract_website_text(url: str) -> str:
    """
    Accesses a website and extracts its content as clean text.
    Useful for reading documentation, online repositories, or tutorials.
    
    Args:
        url (str): The full URL of the website to scrape.
        
    Returns:
        str: The extracted text content or an error message.
    """
    if not url:
        return "Error: URL parameter cannot be empty."

    try:
        # Initialize Fetcher to handle dynamic rendering and bypass anti-bot measures
        fetcher = Fetcher()
        page = fetcher.get(url)
        
        # Ensure we have a valid page response before extracting text
        if not page:
            return f"Error: Received empty response from {url}"
            
        return page.text
    except Exception as e:
        # Log specific domain errors if necessary, returning clean string to the LLM
        return f"Failed to access or parse the page. Error details: {str(e)}"

if __name__ == "__main__":
    # Start the MCP communication via standard input/output (stdio)
    mcp.run()