from dotenv import load_dotenv

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from qa_agent import agent
import os
import uuid

load_dotenv()

session_service = InMemorySessionService()  
inital_state ={
    "user_name":"S3",
    "user_preferences":"""
    I like to play badminton.
    My favorite food is apple.


""",
}

APP_NAME="OUR BOT"
USER_ID="XYZ"
SESSION_ID=str(uuid.uuid4())

stateful_service=session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=inital_state,
)

print("SESSION CREATED ")
print(f"SESSIION ID {SESSION_ID}")


runner=Runner(
    agent=agent,
    app_name=APP_NAME,
    session_service=session_service,
)

new_message=types.Content(
    role="user",
    parts=[types.Part(text="What is S3 favorite food")]

)

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Responces : {event.content.parts[0].text}")

print("===== SESSION EVENET EXPLORED ====")
session =session_service.get_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,


)
print("=== FINAL STAETE ====")

for key,value in session.state.items():
    print(f"key={key} value ={value}")