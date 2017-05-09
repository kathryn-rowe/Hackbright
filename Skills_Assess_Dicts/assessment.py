"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.
    """
    # Seperate the phrase into seperate words.
    words = phrase.split(" ")
    
    word_counts = {}

    # Counts each word and puts it in the Word_counts dictionary with the word
    # as the key and the count as the value.
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon."""

    # Dictionary of melon names and prices
    melon_dict = {"Watermelon": 2.95,
                  "Cantaloupe": 2.50,
                  "Musk": 3.25,
                  "Christmas": 14.25}

    # If the melon is in the dictionary, find its value/price.
    if melon_name in melon_dict:
        return melon_dict[melon_name]
    else:
        return "No price found"


def word_length_sorted(words):
    """Return list of word-lengths and words."""

    word_length_dict = {}

    #creates dictionary to bind word length to words of that length
    for word in words:
        word_length = len(word)
        if word_length not in word_length_dict:
            word_length_dict[word_length] = []
            word_length_dict[word_length].append(word)
        else:
            word_length_dict[word_length].append(word)

    list_len_word_tuples = []

    # Puts the key and corresponding values into tuples, and then puts in list.
    for key, value in word_length_dict.items():
        tuple_word = key, sorted(value)
        list_len_word_tuples.append(tuple(tuple_word))

    return sorted(list_len_word_tuples)


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.
    """
    pirate_dictionary = {"sir": "matey",
                         "hotel": "fleabag inn",
                         "student": "swabbie",
                         "man": "matey",
                         "professor": "foul blaggart",
                         "restaurant": "galley",
                         "your": "yer",
                         "excuse": "arr",
                         "students": "swabbies",
                         "are": "be",
                         "restroom": "head",
                         "my": "me",
                         "is": "be"}
    # Seperate string into seperate words.
    word_line = ""

    for item in phrase:
        word_line = word_line + item

    word_line = word_line.split()

    # Iterate through words to see if they are in Pirate Dictionary. If in dictionary
    # change word to pirate word, otherwise keep word in sentence.
    pirate_sentence = ""

    for word in word_line:
        if word in pirate_dictionary:
            pirate_sentence += pirate_dictionary[word] + " "
        else:
            pirate_sentence += word + " "

    return pirate_sentence.rstrip()

# NOTE: This is a function I had to comment out. I have many questions about it
# and could not get it to work.
# def kids_game(names):
#     """Play a kids' word chain game.

#     Given a list of names, like::

#       bagon baltoy yamask starly nosepass kalob nicky

#     Do the following:

#     1. Always start with the first word ("bagon", in this example).

#     2. Add it to the results.

#     3. Use the last letter of that word to look for the next word.
#        Since "bagon" ends with n, find the *first* word starting
#        with "n" in our list --- in this case, "nosepass".

#     4. Add "nosepass" to the results, and continue. Once a word has
#        been used, it can't be used again --- so we'll never get to
#        use "bagon" or "nosepass" a second time.

#     5. When you can't find an unused word to use, you're done!
#        Return the list of output words.

#     For example::

#         >>> kids_game(["bagon", "baltoy", "yamask", "starly",
#         ...            "nosepass", "kalob", "nicky", "booger"])
#         ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

#     (After "baltoy", there are no more y-words, so we end, even
#     though "nicky" and "booger" weren't used.)

#     Two more examples:

#         >>> kids_game(["apple", "berry", "cherry"])
#         ['apple']

#         >>> kids_game(["noon", "naan", "nun"])
#         ['noon', 'naan', 'nun']

#     This is a tricky problem. In particular, think about how using
#     a dictionary (with the super-fast lookup they provide) can help;
#     good solutions here will definitely require a dictionary.
#     """
#     # name_dictionary = {}

#     # value = 1

#     # for name in names:
#     #     name_dictionary[value] = name
#     #     value += 1

#     # word_list = []

#     # first_word = name_dictionary.get(1)
#     # word_list.append(first_word)
#     # last_letter = first_word[-1]
#     # del name_dictionary[1]


#     # for key, value in name_dictionary.items():
#     #     if value.startswith(last_letter):
#     #         last_letter = value[-1]
#     #         word_list.append(value)
#     #         del name_dictionary[key]
#     # for key, value in name_dictionary.items():
#     #     if value.startswith(last_letter):
#     #         last_letter = value[-1]
#     #         word_list.append(value)
#     #         del name_dictionary[key]
#     # for key, value in name_dictionary.items():
#     #     if value.startswith(last_letter):
#     #         last_letter = value[-1]
#     #         word_list.append(value)
#     #         del name_dictionary[key]

#     # return word_list

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
