from google.adk.agents import Agent
from datetime import datetime
# from google.adk.tools import Tool
# a custom tool that can be used by the agent
def datetime_tool()->dict:
   """Get the current date and time."""
   return {"current_datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="An agent that use tools to answer the user's query.",
    instruction="You are an agent,that use tools for the answers.",
    tools=[datetime_tool],  # Register the datetime tool

)
