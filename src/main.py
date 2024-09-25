# main.py: Entry point for the application; handles incoming webhook requests.

from fastapi import FastAPI, Request
from src.messaging import send_message
from src.database import insert_conversation
from datetime import datetime

app = FastAPI()

@app.post('/webhook')
async def webhook(request: Request):
    data = await request.form()
    message_body = data.get('Body')
    from_number = data.get('From')

    # Process the message and generate a response
    response_text = "Thanks for your message!"

    # Send a reply
    send_message(response_text)

    # Store the conversation
    insert_conversation(
        user_id=from_number,
        timestamp=datetime.now().isoformat(),
        type='incoming',
        summary=message_body
    )

    return 'OK'