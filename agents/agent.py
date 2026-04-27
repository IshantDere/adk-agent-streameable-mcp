import os
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")


notion_mcp_tool = McpToolset(
    connection_params=StreamableHTTPServerParams(
        url="https://mcp.notion.com/mcp"
    ),
)

notion_agent = Agent(
    name="notion_agent",
    model=MODEL_NAME,
    instruction="Connect your Notion workspace to search, update, and power workflows across tools.",
    tools=[notion_mcp_tool],
)


figma_mcp_tool = McpToolset(
    connection_params=StreamableHTTPServerParams(
        url="https://mcp.figma.com/mcp"
    ),
)

figma_agent = Agent(
    name="figma_agent",
    model=MODEL_NAME,
    instruction="Answer questions about the user's Figma workspace.",
    tools=[figma_mcp_tool],
)


slack_mcp_tool = McpToolset(
    connection_params=StreamableHTTPServerParams(
        url="https://mcp.slack.com/mcp"
    ),
)

slack_agent = Agent(
    name="slack_agent",
    model=MODEL_NAME,
    instruction="Answer questions about the user's Slack workspace.",
    tools=[slack_mcp_tool],
)


root_agent = Agent(
    name="main_agent",
    model=MODEL_NAME,
    instruction="""
You are a helpful assistant that can answer questions about the user's Notion, Figma, and Slack workspaces.

Use:
- notion_agent for Notion tasks
- figma_agent for Figma tasks
- slack_agent for Slack tasks

If a query spans multiple tools, use all relevant agents.
""",
    sub_agents=[notion_agent, figma_agent, slack_agent],
)

agent = root_agent