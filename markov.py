import os
import markovify
from twitter import *



with open('copenglish.txt') as f:
    text = f.read()

text_model = markovify.Text(text)

def chain():
    tweet = text_model.make_short_sentence(140)
    return tweet

def tweet():
    auth = OAuth(
    consumer_key = os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET'],
    token = os.environ['TWITTER_TOKEN'],
    token_secret = os.environ['TWITTER_TOKEN_SECRET'],
    )

    t = Twitter(auth=auth)
    t.statuses.update(status=chain())

if __name__ == '__main__':
    tweet()
