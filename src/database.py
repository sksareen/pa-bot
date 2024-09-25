# src/database.py: Handles database connections and queries to Supabase

from supabase import create_client
from src.config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_conversation(user_id, timestamp, type, summary):
    return supabase.table('conversations').insert({
        'user_id': user_id,
        'timestamp': timestamp,
        'type': type,
        'summary': summary
    }).execute()

# Add more database functions as needed