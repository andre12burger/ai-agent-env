# ai-agent-env

A robust, cross-platform environment setup for supercharging local Large Language Models (LLMs) and AI agents (like Cline/Claude Dev) with external tools. 

This repository automates the installation and configuration of Model Context Protocol (MCP) servers and essential AI coding tools (such as Aider, Scrapling, and REA). By leveraging Conda and the ultra-fast `libmamba` solver, it ensures a reproducible, isolated, and conflict-free environment across different machines and operating systems.

## 🎯 Purpose

Running local LLMs requires efficient resource management. This repository separates the "tooling" layer from the "inference" layer. It automatically:
1. Creates a dedicated Python environment (`cline-tools`) for your AI utilities.
2. Installs essential MCP servers and autonomous agents.
3. Automatically maps these tools into your VS Code (Cline) global storage, instantly giving your local models access to web scraping, repository analysis, and reverse engineering capabilities.

## ⚙️ Prerequisites

* **Conda**: You must have Conda installed on your system (Miniconda or Anaconda).
* **VS Code & Cline**: The installation scripts are designed to inject configurations directly into the Cline extension for VS Code.

## 🚀 Installation

Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/ai-agent-env.git
cd ai-agent-env
```

### Windows
Simply execute the batch script. It will configure the Conda solver, build the environment, and copy the MCP settings to your `%APPDATA%` directory.
```cmd
install_windows.bat
```

### Linux / Ubuntu
Make the script executable and run it. It will set up the environment and copy the settings to your `~/.config` directory.
```bash
chmod +x install_linux.sh
./install_linux.sh
```

## 📂 Directory Structure

```text
ai-agent-env/
├── .gitignore                  # Ignores Python caches and temporary AI files
├── cline_mcp_settings.json     # The core MCP routing configuration for Cline
├── environment.yaml            # Conda environment recipe and dependencies
├── install_linux.sh            # Automated setup script for Linux environments
└── install_windows.bat         # Automated setup script for Windows environments
```

## 🧠 Under the Hood: The `libmamba` Solver

Standard Conda dependency resolution can become extremely slow or freeze when dealing with complex Python packages. This repository's installation scripts are designed to automatically inject and configure the `conda-libmamba-solver` before creating the environment. This ensures lightning-fast installations and prevents the dreaded "Solving environment: unsuccessful initial attempt" loop, adhering to principles of robust and reliable deployments.

## 🛠️ Adding New Tools and Capabilities

This environment is designed to be highly extensible. To add new tools to your AI agent:

1. **Add the Dependency**: Open `environment.yaml` and add your new tool under the `pip` or `conda` dependencies list.
2. **Map the Route**: Open `cline_mcp_settings.json` and define how the tool should be executed via the Model Context Protocol.
3. **Re-run the Setup**: Simply run `install_windows.bat` or `install_linux.sh` again. The `--force` flag in the script will cleanly rebuild the environment, and the new settings will be instantly synced to VS Code.