import os
import random

import markovify
from twitter import OAuth, Twitter

DISALLOW_LIST = [None, "none", "None"]


with open("copCombined.txt") as f:
    text = f.read()

text_model = markovify.Text(text)


def generate_tweet():
    max_char = 280
    for _i in range(10):
        tweet_length = random.randint(1, max_char)
        tweet = text_model.make_short_sentence(tweet_length)
        print(tweet)
        if tweet in DISALLOW_LIST:
            continue
        break
    return tweet or " "


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
