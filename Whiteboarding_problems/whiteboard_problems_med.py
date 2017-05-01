def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?
    >>> is_anagram_of_palindrome("a")
    True
    >>> is_anagram_of_palindrome("ab")
    False
    >>> is_anagram_of_palindrome("aab")
    True
    >>> is_anagram_of_palindrome("arceace")
    True
    >>> is_anagram_of_palindrome("arceaceb")
    False
    """

    seen = {}

    # Count each letter

    for letter in word:
        seen[letter] = seen.get(letter, 0) + 1

    seen_an_odd = 0

    for count in seen.values():
        if count % 2 != 0:
            seen_an_odd += 1

    if seen_an_odd > 1:
        return False

    return True


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?
    >>> has_balanced_parens("()")
    True
    >>> has_balanced_parens("(Oh Noes!)(")
    False
    >>> has_balanced_parens("((There's a bonus open paren here.)")
    False
    >>> has_balanced_parens(")")
    False
    >>> has_balanced_parens("(")
    False
    >>> has_balanced_parens("(This has (too many closes.) ) )")
    False
    >>> has_balanced_parens("Hey...there are no parens here!")
    True
    """

    stack = []

    for item in phrase:
        if stack == [] and item == ")":
            return False
        elif item == "(":
            stack.append(item)
        elif item == ")":
            stack.pop()

    if len(stack) == 0:
        return True

    return False


def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.
    >>> binary_search(50)
    1
    >>> binary_search(25)
    2
    >>> binary_search(75)
    2
    >>> binary_search(31) <= 7
    True
    >>> max([binary_search(i) for i in range(1, 101)])
    7
    """

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0
    low = 0
    high = 101
    guess = None

    while guess != val:
        num_guesses += 1
        guess = (high - low) / 2 + low

        if val > guess:
            low = guess

        elif val < guess:
            high = guess

    return num_guesses


def count_recursively(lst):
    """Return number of items in a list, using recursion.
    >>> count_recursively([])
    0
    >>> count_recursively([1, 2, 3])
    3
    """
    if lst == []:
        return 0
    else:
        return 1 + count_recursively(lst[1:])


def decode(s):
    """Decode a string. MY HB ADMISSIONS' PROBLEM!! :)
    >>> decode("0h")
    'h'
    >>> decode("2abh")
    'h'
    >>> decode("0h1ae2bcy")
    'hey'
    """
    letters = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            i = i + int(s[i]) + 1
        else:
            letters += s[i]
            i += 1

    return letters


def missing_number(numbers, max_num):
    """takes this list of numbers, as well as the max_num, and returns the missing number.
    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8
    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8
    """
    numbers.sort()

    if numbers[-1] != max_num:
        return numbers[-1]

    count = max_num - (max_num - 1)

    for num in numbers:
        if count != num:
            return count
        count += 1


def find_mode(nums):
    """Find the most frequent num(s) in nums.
    >>> find_mode([1]) == {1}
    True
    >>> find_mode([1, 2, 2, 2]) == {2}
    True
    >>> find_mode([1, 1, 2, 2]) == {1, 2}
    True
    """
    counts = {}
    modes = set()

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    largest = counts[nums[0]]

    for key, value in counts.iteritems():
        if value > largest:
            largest = value

    for key, value in counts.iteritems():
        if value == largest:
            modes.add(key)

    return modes


def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place.
    >>> print_digits(1)
    1
    >>> print_digits(314)
    4
    1
    3
    >>> print_digits(12)
    2
    1
    """

    while num > 0:
        tenths = num % 10
        num = num / 10
        print tenths


def print_recursively(lst):
    """Print items in the list, using recursion.
    >>> print_recursively([1, 2, 3])
    1
    2
    3
    """
    if lst == []:
        return None

    print lst[0]

    print_recursively(lst[1:])


def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.
    Return None if needle is not in haystack. Do this with recursion.
    >>> lst = ["hey", "there", "you"]
    >>> recursive_index("hey", lst)
    0
    >>> recursive_index("you", lst)
    2
    >>> recursive_index("porcupine", lst) is None
    True
    """
    def _recursive_index(needle, haystack, start_at):
        if start_at == len(haystack):
            return None

        if haystack[start_at] == needle:
            return start_at

        return _recursive_index(needle, haystack, start_at + 1)

    return _recursive_index(needle, haystack, 0)


class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.
        >>> Node(3).as_string()
        '3'
        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


def remove_node(node):
    """Given a node in a linked list, remove it.
    Remove this node from a linked list. Note that we do not have access to
    any other nodes of the linked list, like the head or the tail.
    Does not return anything; changes list in place.

    >>> four_node = Node(4)
    >>> three_node = Node(3, four_node)
    >>> two_node = Node(2, three_node)
    >>> one_node = Node(1, two_node)
    >>> one_node.as_string()
    '1234'
    >>> remove_node(two_node)
    >>> one_node.as_string()
    '134'
    """
    if not node.next:
        raise ValueError("Cannot remove tail node")

    node.data = node.next.data
    node.next = node.next.next


def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    >>> rev_string("porcupine")
    'enipucrop'
    >>> rev_string("ab")
    'ba'
    """
    if len(astring) == 1:
        return astring[0]

    return astring[-1] + rev_string(astring[:-1])

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
