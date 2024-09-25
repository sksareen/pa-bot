# src/scheduler.py: Sets up scheduled tasks for message sending.

import schedule
import time
from src.messaging import send_message

def morning_check_in():
    send_message("Good morning! How did you sleep?")

def lunch_check_in():
    send_message("Hey! How's your day going so far?")

def evening_reflection():
    send_message("Good evening! How was your day?")

# Schedule messages
schedule.every().day.at("07:30").do(morning_check_in)
schedule.every().day.at("12:00").do(lunch_check_in)
schedule.every().day.at("18:00").do(evening_reflection)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)