from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

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

    while key in chains:
        word_two = key[1]
        word_three = choice(chains[key])
        #word_four = choice(chains[key])
        text += " " + word_three
        key = (word_two, word_three)

    # import pprint
    # pprint.pprint(chains)
        return text

input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# # # Produce random text
random_text = make_text(chains)

print random_text
