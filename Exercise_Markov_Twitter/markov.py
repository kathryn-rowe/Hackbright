from random import choice
import sys
import os
import twitter


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    #file_path = sys.argv[1]
    input_text = open(file_path).read()

    return input_text

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    words = text_string.split()

    chains = {}
    #this finds how many words to put in the n_gram tuple
    #n_gram = int(raw_input("How many words do you want in your n_gram?: "))

    #tuple_n_gram = tuple(words[:n_gram])

    #print tuple_n_gram

    for i in range(len(words) - 2):
        tuple_bi_gram = words[i], words[i + 1]
        following_word = words[i + 2]
        chains[tuple_bi_gram] = chains.get(tuple_bi_gram, [])
        chains[tuple_bi_gram].append(following_word)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    key = choice(chains.keys())

    # if key == key[0].title():

    text = " ".join(key)
    #need to change this to coorespond with how many words are going in the n_gram tuple.
    while key in chains:
        word_one = key[0]
        word_two = key[1]
        word_three = choice(chains[key])
        #word_four = choice(chains[key])
        text += " " + word_three
        key = (word_two, word_three)

    # import pprint
    # pprint.pprint(chains)

    return text[0:140]


file_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(file_path)

# Get a Markov chain
chains = make_chains(input_text)

# # # Produce random text
random_text = make_text(chains)

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

#print api.VerifyCredentials()

while True:
    source_code_confirmation = raw_input("Did you source the codes? If you did, hit enter. If not, press q")
    if source_code_confirmation == "q":
        break
    else:
        status = api.PostUpdate(make_text(chains))
        print status.text

        user_update_input = raw_input("Enter to tweet again [q to quit] > ")

        if user_update_input == "q" or user_update_input == "Q":
            break
        else:
            status = api.PostUpdate(make_text(chains))
            print status.text
