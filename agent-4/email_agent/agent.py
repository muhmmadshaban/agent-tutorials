from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
import random
load_dotenv()

class EmailContent(BaseModel):
    subject: str = Field( description="The subject of the email. Should be concise and relevant to the body content.")
    body: str = Field( description="The main content of the email. Should be with proper greeting, paragraph and the signature.")


model=LiteLlm(
    model="gemini-2.0-flash",
    max_tokens=1000,
    temperature=0.1,
    api_key=os.getenv("GOOGLE_API_KEY")
)



agent = Agent(
    name="email_agent",
    model="gemini-2.0-flash",
    description="Generate an email based on the provided content.",
    instruction="""
    You are an email generator assistant.
    Your task is to generate an email based on the provided content.
    
    GUIDLINES:
    1. The email should have a proper greeting, body content, and signature.
    2. Create a subject line that is concise and relevant to the body content.
    3. The body should be well-structured with paragraphs.
    4. Use a professional tone and format.
    5. Ensure the email is clear and easy to read.
    6. The email should be in English.
    7. Email should be concise and to the point and complete.
    8. Suggest relevent attachments if needed.

    IMPORTANT:
    Your response should be a valid JSON object with the following structure:
    {
        "subject": "Your subject here",
        "body": "Your email body here"}

    DO NOT include any additional text or explanations outside of the JSON object.
    """,
    output_schema=EmailContent,
    output_key="email_content",


)
