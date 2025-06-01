from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv
import os
import random
load_dotenv()

# this is complete working agent code, but we need a google billing account to run this code,
"""
This agent uses Google's ADK and Gemini LLM to generate jokes.
You must have a valid Google API key and an active billing account to use this agent.
If billing is not enabled, you will receive an error message and the agent will not function.
Make sure to set your GOOGLE_API_KEY in a .env file or environment variable.
"""

model=LiteLlm(
    model="gemini-2.0-flash",
    max_tokens=1000,
    temperature=0.1,
    api_key=os.getenv("GOOGLE_API_KEY")
)


def jokes():
    joke=[
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!"

    ]
    return random.choice(joke)

agent = Agent(
    name="joke_agent",
    model=model,
    description="Joke Agent",
    instruction="You are a helpful assistant that tells jokes. When the user asks for a joke, only use the tool 'jokes' to tell jokes.",
    tools=[jokes], 

)
