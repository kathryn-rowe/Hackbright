import string


def count_words(filename):
    """Opens file and counts how many times a word occurs in that file."""
    all_words = []

    for row in open(filename):
        row = row.rstrip()
        words = row.split(" ")
        for word in words:
            new_word = word.strip(string.punctuation)
            all_words.append(new_word)

    count_dict = {}

    for word in all_words:
        count_dict[word] = count_dict.get(word, 0) + 1

    for key, value in count_dict.iteritems():
        print key, value

count_words("test.txt")
