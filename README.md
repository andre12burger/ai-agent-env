# AI Agent Environment 🤖

A robust, zero-configuration environment setup for supercharging local Large Language Models (LLMs) and AI agents (like Cline/Claude Dev) with external tools. 

This repository automates the configuration of Model Context Protocol (MCP) servers and essential AI coding tools (such as Aider, Scrapling, and REA). By leveraging the ultra-fast `uv` package manager and standard `pyproject.toml` specifications, it ensures a reproducible, isolated, and lightning-fast environment across different machines and operating systems without polluting your system Python.

## 🎯 Purpose

Running local LLMs requires efficient resource management. This repository separates the "tooling" layer from the "inference" layer. It automatically maps powerful autonomous capabilities into your VS Code (Cline) global storage, instantly giving your local models access to web scraping, repository analysis, and reverse engineering capabilities via `uvx` ephemeral execution.

## ⚙️ Prerequisites

* **uv**: You must have Astral's `uv` package manager installed (`curl -LsSf https://astral.sh/uv/install.sh | sh` or via PowerShell).
* **VS Code & Cline**: The installation scripts are designed to inject configurations directly into the Cline extension for VS Code.

## 🚀 Setup & Synchronization

Clone this repository to your local machine:
```bash
git clone [https://github.com/andre12burger/ai-agent-env.git](https://github.com/andre12burger/ai-agent-env.git)
cd ai-agent-env

```

### Windows

Simply execute the sync script. It will automatically copy the optimized MCP settings to your `%APPDATA%` directory. The `uv` manager will handle the dependencies on the fly when the tools are first invoked by the AI.

```cmd
sync_mcp.bat

```

## 📂 Directory Structure

```text
ai-agent-env/
├── config/
│   └── cline_mcp_settings.json  # The core MCP routing configuration for Cline using uvx
├── src/
│   ├── ai_agent_env/            # Python module initialization
│   └── scrapling_server.py      # Custom FastMCP server for web scraping
├── .gitignore                   # Ignores Python caches and temporary AI files
├── pyproject.toml               # Official Python project specification and dependencies
├── README.md                    # Project documentation
└── sync_mcp.bat                 # Automated VS Code routing sync script

```

## 🛠️ Adding New Tools and Capabilities

This environment is designed to be highly extensible. To add new tools to your AI agent:

1. **Add the Dependency**: Run `uv add <package_name>` to automatically update the `pyproject.toml`.
2. **Map the Route**: Open `config/cline_mcp_settings.json` and define the tool execution via the Model Context Protocol using `uvx` (for standalone binaries) or `uv run` (for custom scripts).
3. **Re-run the Sync**: Execute `sync_mcp.bat` to instantly apply the new capabilities to VS Code.

```
