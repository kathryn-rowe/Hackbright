def count_words(words_file):
    """Takes a file and counts word occurrence."""

    words_list = open(words_file)

    all_words_list = []

    for line in words_list:
        # phrase = words_string.append(line)
        line = line.rstrip()
        words_in_line = line.split(" ")
        for word in words_in_line:
            all_words_list.append(word)

    words_count = {}

    for word in all_words_list:
        words_count[word] = words_count.get(word, 0) + 1

    def get_count(word):
        return words_count.get(word, 0)

    #print get_count("met")

count_words("test.txt")
