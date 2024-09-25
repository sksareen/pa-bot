# src/config.py: Stores configuration variables and API keys.

import os
from dotenv import load_dotenv

# Load environment variables from .env.local
load_dotenv('.env.local')

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Supabase configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# User configuration
USER_PHONE_NUMBER = os.getenv('USER_PHONE_NUMBER')