from dotenv import load_dotenv
from utils import call_agent_async
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from google.genai import types
from memory_agent import agent
import os
import uuid

load_dotenv()

db_url="sqlite:///./session.db"
session_service = DatabaseSessionService(db_url=db_url)
inital_state = {
    "user_name": "S3",
    "reminders":[],
}

async def main_async():
    APP_NAME = "MEMORY BOT"
    USER_ID = "XYZ"

    existing_session = session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID,
    )

    if existing_session and len(existing_session.sessions) > 0:
        SESSION_ID = existing_session.sessions[0].id
        print(f"Using existing session: {SESSION_ID}")
    else:
        new_session = session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=inital_state,
        )
        SESSION_ID = new_session.id
        print(f"Created new session: {SESSION_ID}")



    runner=Runner(
        agent=agent,
        app_name=APP_NAME,
        session_service=session_service, 
    )
    print("Welcome to the Memory Bot!")
    print("Type 'exit' to end the chat.")
    print("You can ask me to remember things for you, like reminders or preferences.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting the chat.")
            break
        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main_async())

        