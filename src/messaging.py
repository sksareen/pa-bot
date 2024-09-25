# src/messaging.py: Contains functions for sending messages via Twilio.

from twilio.rest import Client
from src.config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, USER_PHONE_NUMBER

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_message(body):
    message = client.messages.create(
        body=body,
        from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
        to=f'whatsapp:{USER_PHONE_NUMBER}'
    )
    return message.sid