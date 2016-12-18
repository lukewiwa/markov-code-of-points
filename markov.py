import markovify
from twitter import *

auth = OAuth(
consumer_key = 'TWITTER_CONSUMER_KEY',
consumer_secret = 'TWITTER_CONSUMER_SECRET',
token = 'TWITTER_TOKEN',
token_secret = 'TWITTER_TOKEN_SECRET',
)

t = Twitter(auth=auth)

with open('copenglish.txt') as f:
    text = f.read()

text_model = markovify.Text(text)

def sentences(repeats=1):
    for i in range(repeats):
        print(text_model.make_short_sentence(140))

t.statuses.update(status=sentences())

if __name__ == '__main__':
    sentences()
