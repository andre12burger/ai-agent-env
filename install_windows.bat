@echo off
echo [1/3] Criando ambiente Conda com otimizacao libmamba...
conda config --set solver libmamba
conda env create -f environment.yml --force

echo [2/3] Configurando rotas MCP no Cline (VS Code)...
if not exist "%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings" mkdir "%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings"
copy /Y "config\cline_mcp_settings.json" "%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json"

echo [3/3] Instalacao concluida!
pause