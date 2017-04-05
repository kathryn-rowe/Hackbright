import string


def count_words(words_file):
    """Takes a file and counts word occurrence."""

    words_list = open(words_file)

    all_words_list = []

    for line in words_list:
        line = line.rstrip()
        # line = line.strip(string.punctuation)
        # line.translate(None, string.punctuation)
        words_in_line = line.split(" ")
        for word in words_in_line:
            new_word = word.strip(string.punctuation)
            all_words_list.append(new_word)

    words_count = {}

    for word in all_words_list:
        words_count[word] = words_count.get(word, 0) + 1

    # def get_count(word):
    #     return words_count.get(word, 0)

    #print get_count("met")


    for item, count in words_count.iteritems():
        print "%s, %d" % (item, count)

count_words("twain.txt")
