@echo off
echo Sincronizando rotas MCP para o Cline...
if not exist "%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings" mkdir "%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings"
copy /Y "config\cline_mcp_settings.json" "%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json"
echo Rotas atualizadas com sucesso!
pause
