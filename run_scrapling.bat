@echo off
REM Ativa o ambiente isolado do Conda e executa o servidor MCP do Scrapling
call conda activate cline-tools
python src\scrapling_server.py