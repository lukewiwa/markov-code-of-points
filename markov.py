import os
import markovify
from twitter import *



with open('copenglish.txt') as f:
    text = f.read()

text_model = markovify.Text(text)

def sentences(repeats=1):
    for i in range(repeats):
        print(text_model.make_short_sentence(140))

def tweet():
    auth = OAuth(
    consumer_key = os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET'],
    token = os.environ['TWITTER_TOKEN'],
    token_secret = os.environ['TWITTER_TOKEN_SECRET'],
    )

    t = Twitter(auth=auth)
    t.statuses.update(status=sentences())

if __name__ == '__main__':
    tweet()
