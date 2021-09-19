import os
import random

import markovify
from twitter import OAuth, Twitter


with open("copCombined.txt") as f:
    text = f.read()

text_model = markovify.Text(text)


def generate_tweet():
    max_char = 280
    min_char = 5
    tweet_length = random.randint(min_char, max_char)
    return text_model.make_short_sentence(tweet_length, min_chars=min_char)


def tweet():
    auth = OAuth(
        consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
        consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
        token=os.getenv("TWITTER_TOKEN"),
        token_secret=os.getenv("TWITTER_TOKEN_SECRET"),
    )

    t = Twitter(auth=auth)
    t.statuses.update(status=generate_tweet())


def handler(event, context):
    tweet()
