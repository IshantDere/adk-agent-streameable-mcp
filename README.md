# ADK MCP Multi-Agent FastAPI Server

A production-ready **Google ADK MCP Multi-Agent Server** built with **FastAPI**, **Docker**, and **MCP tools** for integrating external workspaces like:

- Notion
- Figma
- Slack

This project uses a root agent that intelligently routes user queries to the correct sub-agent.

---

## Features

- Google ADK Agent Architecture
- MCP Tool Integration
- Multi-Agent Routing
- FastAPI REST API
- Dockerized Deployment
- Environment Variable Based Model Selection
- Production Ready Structure

---

## Project Structure

```bash
.
├── agents/
│   ├── __init__.py
│   └── agent.py
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── test.sh