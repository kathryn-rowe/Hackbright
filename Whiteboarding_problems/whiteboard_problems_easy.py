import random


def add_to_zero(lst):
    """Given list of ints, return True if any two nums in list sum to 0.
    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True
    """

    for num in lst:
        if num == 0:
            return True
        elif -num in lst:
            return True
    return False


def concat_lists(lst1, lst2):
    """Given two lists. concatenate them (that is, combine them into a single list).

    >>> concat_lists([], [1, 2])
    [1, 2]

    >>> concat_lists([1, 2], [])
    [1, 2]

    >>> concat_lists([], [])
    []
    """

    if len(lst1) == 0 and len(lst2) == 0:
        return []
    for num in lst2:
        lst1.append(num)
    return lst1


def is_leap_year(year):
    """Is this year a leap year?

    >>> is_leap_year(1904)
    True

    >>> is_leap_year(1900)
    False

    >>> is_leap_year(2000)
    True
    """

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True


def days_in_month(date):
    """How many days are there in a month?

    >>> days_in_month("02 2015")
    28
    """

    month, year = date.split(" ")

    month_year = {1: 31,
                  2: 28,
                  3: 31,
                  4: 30,
                  5: 31,
                  6: 30,
                  7: 31,
                  8: 31,
                  9: 30,
                  10: 31,
                  11: 30,
                  12: 31}
    year = int(year)
    month = int(month)

    if is_leap_year(year):
        days = month_year[02]
        days -= 1

    days = month_year[month]

    return days


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).

    >>> lucky_numbers(0)
    []
    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    randoms = set()

    while len(randoms) < n:
        number = random.randint(1, 10)
        randoms.add(number)

    randoms = list(randoms)
    return randoms


def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple.
    >>> find_range([3, 4, 2, 5, 10])
    (2, 10)

    >>> find_range([43, 3, 44, 20, 2, 1, 100])
    (1, 100)

    >>> find_range([])
    (None, None)

    >>> find_range([7])
    (7, 7)
    """

    if len(nums) == 0:
        return (None, None)

    nums.sort()

    largest = nums[-1]
    smallest = nums[0]

    # for num in nums:
    #     if num > largest:
    #         largest = num
    #     elif num < smallest:
    #         smallest = num

    return (smallest, largest)


def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion.
    >>> fizzbuzz()
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    17
    fizz
    19
    buzz
    """

    for num in range(1, 21):
        if num % 3 == 0 and num % 5 == 0:
            print "fizzbuzz"
        elif num % 3 == 0:
            print "fizz"
        elif num % 5 == 0:
            print "buzz"
        else:
            print num


def has_more_vowels(word):
    """Does word contain more vowels than non-vowels?
    >>> has_more_vowels("moose")
    True

    >>> has_more_vowels("mice")
    False

    >>> has_more_vowels("graph")
    False

    >>> has_more_vowels("yay")
    False

    >>> has_more_vowels("Aal")
    True
    """
    vowels = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}

    word = word.lower()

    vowel_count = 0
    non_vowel = 0

    for letter in word:
        if letter in vowels:
            vowel_count += 1
        else:
            non_vowel += 1

    if vowel_count > non_vowel:
        return True

    return False


def has_unique_chars(word):
    """Does word contains unique set of characters?
    >>> has_unique_chars("Monday")
    True

    >>> has_unique_chars("Moonday")
    False

    >>> has_unique_chars("")
    True

    >>> has_unique_chars("Bob")
    True
    """
    letter_count = {}

    for letter in word:
        if letter in letter_count:
            return False
        else:
            letter_count[letter] = 1

    return True


def is_prime(num):
    """Is a number a prime number?
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(11)
    True
    >>> is_prime(999)
    False
    """
    x = 2

    if num <= 1:
        return False

    while (x * x) <= num:
        if num % x == 0:
            return False
        x += 1

    return True


def is_palindrome(word):
    """Return True/False if this word is a palindrome.
    >>> is_palindrome("a")
    True
    >>> is_palindrome("noon")
    True
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("porcupine")
    False
    >>> is_palindrome("Racecar")
    False
    """

    reverse_word = word[::-1]

    if reverse_word == word:
        return True

    return False


def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number.
    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
    2
    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
    4
    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
    1
    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
    2
    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10) is None
    True
    """

    if nums[0] > xnumber:
        return None

    largest = nums[0]

    for num in nums:
        if num <= xnumber and num >= largest:
            largest = num
            index = nums.index(num)

    return index


def translate_leet(phrase):
    """Translates input into "leet-speak".
    >>> translate_leet("Hi Balloonicorn")
    'Hi B@1100nic0rn'
    >>> translate_leet("Hackbright is the Shizzle")
    'H@ckbrigh7 i5 7h3 5hizz13'
    """
    leet_speek = {"a": "@",
                  "o": 0,
                  "e": 3,
                  "l": 1,
                  "s": 5,
                  "t": 7}

    leet_phrase = ""

    for letter in phrase:
        lower_let = letter.lower()
        if lower_let in leet_speek:
            leet_phrase += str(leet_speek[lower_let])
        else:
            leet_phrase += str(letter)

    return leet_phrase


def find_longest_word(words):
    """Return longest word in list of words.
    >>> find_longest_word(["hi", "hello"])
    5
    >>> find_longest_word(["Balloonicorn", "Hackbright"])
    12
    """
    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = len(word)

    return longest


def max_num(num_list):
    """Returns largest integer from given list
    >>> max_num([5, 3, 6, 2, 1])
    6
    """
    largest = num_list[0]

    for num in num_list:
        if num > largest:
            largest = num

    return largest


def max_of_three(num1, num2, num3):
    """Returns the largest of three integers
    >>> max_of_three(1, 5, 2)
    5
    >>> max_of_three(10, 1, 11)
    11
    """
    max_num = num1

    if num2 > num1:
        max_num = num2

    if num3 > max_num:
        max_num = num3

    return max_num


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise.
    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    >>> is_pangram("I like cats, but not mice")
    False
    """
    alpha_set = set()

    for letter in sentence:
        if letter != " ":
            alpha_set.add(letter)

    if len(alpha_set) < 26:
        return False

    return True


def pig_latin(phrase):
    """Turn a phrase into pig latin.
    There will be no uppercase letters or punctuation in the phrase.

    If the word begins with a consonant (not a, e, i, o, u), move the first letter to the end and add ay
    If the word begins with a vowel, add yay to the end

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'
    >>> pig_latin('porcupines are cute')
    'orcupinespay areyay utecay'
    >>> pig_latin('give me an apple')
    'ivegay emay anyay appleyay'
    """

    phrase = phrase.split(" ")
    pig_phrase = []
    vowels = set(["a", "e", "i", "o", "u"])

    for word in phrase:
        if word[0] in vowels:
            word += "yay"
            pig_phrase.append(word)
        else:
            first = word[0]
            last = word[1:]
            word = last + first + "ay"
            pig_phrase.append(word)

    return " ".join(pig_phrase)


def deduped(items):
    """Return new list from items with duplicates removed.
    >>> deduped([1, 1, 1])
    [1]
    >>> deduped([1, 2, 1, 1, 3])
    [1, 2, 3]
    >>> deduped([1, 2, 3])
    [1, 2, 3]
    >>> a = [1, 2, 3]
    >>> b = deduped(a)
    >>> a == b
    True
    >>> a is b
    False
    >>> deduped([])
    []
    """
    # remove_dups = set(items)
    # SETS ARE UNORDERED!!! passed tests but can't be relied upon.
    # return list(remove_dups)
    remove_dups = []

    for item in items:
        if item not in remove_dups:
            remove_dups.append(item)

    return remove_dups


def replace_vowels(chars):
    """Given list of chars, return a new copy, but with vowels replaced by '*'.
    >>> replace_vowels(['h', 'i'])
    ['h', '*']
    >>> replace_vowels(['o', 'o', 'o'])
    ['*', '*', '*']
    >>> replace_vowels(['z', 'z', 'z'])
    ['z', 'z', 'z']
    >>> replace_vowels([])
    []
    >>> replace_vowels(["A", "b"])
    ['*', 'b']
    >>> replace_vowels(["y", "a", "y"])
    ['y', '*', 'y']
    """
    vowels = set(["a", "e", "i", "o", "u"])

    new_char = []

    for char in chars:
        low_char = char.lower()
        if low_char in vowels:
            new_char.append("*")
        else:
            new_char.append(char)

    return new_char


def rev_list_in_place(lst):
    """Reverse list in place.
    You cannot do this with reversed(), .reverse(), or list slice
    assignment!
    >>> lst = [1, 2, 3]
    >>> rev_list_in_place(lst)
    >>> lst
    [3, 2, 1]
    """

    for index in range(len(lst)/2):

        index_to_swap = (index + 1) * -1

        # swap values at these indexes
        lst[index], lst[index_to_swap] = lst[index_to_swap], lst[index]


def rev_string(astring):
    """Return reverse of string.

    You may NOT use the reversed() function!
    >>> rev_string("porcupine")
    'enipucrop'
    """
    rev_string = ""

    for item in astring[::-1]:
        rev_string += item

    return rev_string


def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list.
    >>> lst = [1, 2, 3, 4, 6, 8]
    >>> show_evens(lst)
    [1, 3, 4, 5]
    """
    even_index = []

    index = 0

    for num in nums:
        if num % 2 == 0:
            even_index.append(index)
        index += 1

    # for i in range(len(nums)):
    #     if nums[i] % 2 == 0:
    #         even_index.append(i)

    return even_index


def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name.
    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'
    """
    camel = ""
    i = 0
    while i < (len(variable_name)):
        if variable_name[i] == "_":
            next = variable_name[i+1]
            next = next.upper()
            camel += next
            i += 2
        else:
            camel += variable_name[i]
            i += 1

    # HACKBRIGHT SOLUTION
    # words = variable_name.split("_")

    # for i in range(1, len(words)):
    #     words[i] = words[i].capitalize()

    # return "".join(words)

    return camel


def sum_list(num_list):
    """Return the sum of all numbers in list.
    >>> sum_list([5, 3, 6, 2, 1])
    17
    """

    sum_total = 0

    for num in num_list:
        sum_total += num

    return sum_total


def word_count(phrase):
    """Count words in a sentence, and print in ascending order.
    >>> word_count("berry cherry cherry cherry berry apple")
    cherry: 3
    berry: 2
    apple: 1
    >>> word_count("berry cherry cherry cherry berry apple")
    cherry: 3
    berry: 2
    apple: 1
    >>> word_count("hi Hi hi")
    hi: 2
    Hi: 1
    """
    word_count = {}
    phrase_split = phrase.split(" ")

    for word in phrase_split:
        word_count[word] = word_count.get(word, 0) + 1

    for key, value in word_count.iteritems():
        print str(key) + ": " + str(value)


def word_lengths(sentence):
    """Get dictionary of word-length: {words}.
    >>> answer = word_lengths("cute cats chase fuzzy rats")
    >>> sorted(answer.keys())
    [4, 5]
    >>> answer = word_lengths("cute cats chase fuzzy rats")
    >>> answer[4] == {'cute', 'cats', 'rats'}
    True
    >>> answer = word_lengths("cute cats chase fuzzy rats")
    >>> answer[5] == {'chase', 'fuzzy'}
    True
    >>> answer = word_lengths("Hi, I'm Balloonicorn")
    >>> sorted(answer.keys())
    [3, 12]
    >>> answer = word_lengths("Hi, I'm Balloonicorn")
    >>> answer[3] == {'Hi,', "I'm"}
    True
    >>> answer = word_lengths("Hi, I'm Balloonicorn")
    >>> answer[12] == {"Balloonicorn"}
    True
    """
    word_lengths = {}
    sent_split = sentence.split(" ")

    for word in sent_split:
        word_len = len(word)
        if word_len not in word_lengths:
            word_lengths[word_len] = set()

        word_lengths[word_len].add(word)

    return word_lengths


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
