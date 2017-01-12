import os

import twitter

import markov

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

#print api.VerifyCredentials()

while True:
    user_update_input = raw_input("Enter to tweet again [q to quit] > ")
    if user_update_input == "q" or user_update_input == "Q":
        break
    else:
        chains = 'gettysburg.txt'
        status = api.PostUpdate(markov.make_text(chains))
        print status.text
