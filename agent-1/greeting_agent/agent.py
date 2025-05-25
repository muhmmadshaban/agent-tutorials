from google.adk.agents import Agent

agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="An agent that greets the user and provides a friendly response.",
    instruction="You are a helpful assitant that greet the user. Ask the user name and greet them with their name.",

)
