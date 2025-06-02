from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
import random
load_dotenv()


agent = Agent(
    name="qa_agent",
    model="gemini-2.0-flash",
    description="Question Answering agent",
    instruction="""
    You are a helpful assistant that answer the questtion about the user preferences.
    Here is some information about the user:
    Name :
    {user_name}
    Preference:
    {user_preferences}
    """,
 

)
