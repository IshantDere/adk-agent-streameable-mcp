import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams


# Load .env
load_dotenv()

INDEED_MCP_API_KEY = os.getenv("INDEED_MCP_API_KEY")

notion_mcp_tool = McpToolset(
    connection_params=StreamableHTTPServerParams(
        url="https://mcp.notion.com/mcp"
    ),
)

notion_agent = Agent(
    name="indeed_agent",
    model="groq/openai/gpt-oss-120b",
    instruction="Connect your Notion workspace to search, update, and power workflows across tools.",
    tools=[notion_mcp_tool])


figma_mcp_tool = McpToolset(
    connection_params=StreamableHTTPServerParams(
        url="https://mcp.figma.com/mcp"
    ),
)

figma_agent = Agent(
    name="figma_agent",
    model="groq/openai/gpt-oss-120b",
    instruction="Answer questions about the user's Figma workspace.",
    tools=[figma_mcp_tool]
)

slack_mcp_tool = McpToolset(
    connection_params=StreamableHTTPServerParams(
        url="https://mcp.slack.com/mcp"
    ),
)

slack_agent = Agent(
    name="slack_agent",
    model="groq/openai/gpt-oss-120b",
    instruction="Answer questions about the user's Slack workspace.",
    tools=[slack_mcp_tool]
)


root_agent = Agent(
    name="main_agent",
    model="groq/openai/gpt-oss-120b",
    instruction="""
    You are a helpful assistant that can answer questions about the user's Notion, Figma, and Slack workspaces.
    You have access to three agents, notion_agent, figma_agent, and slack_agent, that can answer questions about
    the user's Notion, Figma, and Slack workspaces, respectively. If a question is about Notion, use the notion_agent to answer it. If a question is about Figma, use the figma_agent to answer it. If a question is about Slack, use the slack_agent to answer it. If a question is about both Notion and Figma or all three workspaces, use all relevant agents to answer it.

    """,
    sub_agents=[notion_agent, figma_agent, slack_agent],   
)
