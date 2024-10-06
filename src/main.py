import os
import tweepy
from dotenv import load_dotenv
import time
import openai

# Load environment variables
load_dotenv()

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(
    os.getenv("CONSUMER_KEY"),
    os.getenv("CONSUMER_SECRET")
)
auth.set_access_token(
    os.getenv("ACCESS_TOKEN"),
    os.getenv("ACCESS_TOKEN_SECRET")
)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def check_mentions(api, since_id):
    new_since_id = since_id
    mentions = tweepy.Cursor(api.mentions_timeline, since_id=since_id, tweet_mode='extended').items()
    for tweet in mentions:
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        prompt = f"As an ENTP advisor, respond to this tweet: {tweet.full_text}"
        response = generate_response(prompt)
        try:
            api.update_status(
                status=f"@{tweet.user.screen_name} {response}",
                in_reply_to_status_id=tweet.id,
            )
            print(f"Replied to @{tweet.user.screen_name}")
        except tweepy.TweepError as e:
            print(f"Error replying to @{tweet.user.screen_name}: {e}")
    return new_since_id

def main():
    since_id = 1
    while True:
        since_id = check_mentions(api, since_id)
        time.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == "__main__":
    main()
