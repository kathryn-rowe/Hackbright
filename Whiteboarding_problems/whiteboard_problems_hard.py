class Node(object):  # ...
    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def insert(self, new_data):
        """Insert new node with `new_data` to BST tree rooted here.
        """

        if new_data < self.data:
            if self.left.data is None:
                self.left.data = Node(new_data)
            else:
                self.left.insert(new_data)
        elif new_data > self.data:
            if self.right.data is None:
                self.right.data = Node(new_data)
            else:
                self.right.insert(new_data)


def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    >>> has_balanced_brackets("<ok>")
    True
    >>> has_balanced_brackets("<[ok]>")
    True
    >>> has_balanced_brackets("<[{(yay)}]>")
    True
    >>> has_balanced_brackets("(Oops!){")
    False
    >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
    False
    >>> has_balanced_brackets(">")
    False
    >>> has_balanced_brackets("(This has {too many} ) closers. )")
    False
    >>> has_balanced_brackets("<{Not Ok>}")
    False
    >>> has_balanced_brackets("No brackets here!")
    True
    """
    brackets_open = {"<": 1, "(": 2, "[": 3, "{": 4}
    brackets_close = {">": 1, ")": 2, "]": 3, "}": 4}
    stack = []

    for item in phrase:
        if stack == [] and item in brackets_close:
            return False
        elif item in brackets_open:
            stack.append(brackets_open[item])
        elif item in brackets_close:
            if brackets_close[item] == stack[-1]:
                stack.pop()
            else:
                return False

    return stack == []


class Node3:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def is_valid(self):

        def _ok(n, lt, rt):
            """Check this node & recurse to children

                lt: left children must be <= this
                rt: right child must be >= this
            """

            if n is None:
                # base case
                return True

            if lt is not None and n.data > lt:
                # base case
                return False

            if rt is not None and n.data < rt:
                # base case
                return False

            # FOR THE LEFT SIDE CHECK
            if not _ok(n.left, n.data, rt):
                # general case: check our left child
                #   all descendants of left child must be
                #   less than our data (and greater than
                #   whatever we had to be greater than).
                #   if not, fail fast.
                return False

            if not _ok(n.right, lt, n.data):
                # general case: check our right child
                #   all descendants of right child must be
                #   greater than our data (and less than
                #   whatever we had to be less than)
                #   if not, fail fast.
                return False

            # If we reach here, we're either a leaf node with
            # valid data for lt/gt, or we're higher up, but
            # our recursive calls downward succeeded. Either way,
            # this is our winning base case.
            return True

        # Call our recursive function, starting here.
        # Since we haven't yet gone left or right, we don't know
        # our `lt` or `rt` values yet, so pass None for these.

        return _ok(self, None, None)


def calc(s):
    """Evaluate expression.

    >>> calc("+ 1 2")  # 1 + 2
    3
    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6
    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15
    >>> calc("- 1 2")  # 1 - 2
    -1
    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3
    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
    """
    phrase = s.split(" ")

    total = int(phrase.pop())

    while phrase:
        num = int(phrase.pop())

        operator = phrase.pop()

        if operator == "+":
            total = num + total
        elif operator == "*":
            total = num * total
        elif operator == "-":
            total = num - total
        else:
            total = num / total

    return total


def check(king, queen):
    """Given a chessboard with one K and one Q, see if the K can attack the Q.

    This function is given coordinates for the king and queen on a chessboard.
    These coordinates are given as a letter A-H for the columns and 1-8 for the
    row, like "D6" and "B7":
    >>> check("D6", "H6")
    True
    >>> check("E6", "E4")
    True
    >>> check("B7", "D5")
    True
    >>> check("A1", "H8")
    True
    >>> check("A8", "H1")
    True
    >>> check("D6", "H7")
    False
    >>> check("E6", "F4")
    False
    """
    # board = [["A", "B", "C", "D", "E", "F", "G", "H"],
    #          ["A", "B", "C", "D", "E", "F", "G", "H"],
    #          ["A", "B", "C", "D", "E", "F", "G", "H"],
    #          ["A", "B", "C", "D", "E", "F", "G", "H"],
    #          ["A", "B", "C", "D", "E", "F", "G", "H"],
    #          ["A", "B", "C", "D", "E", "F", "G", "H"],
    #          ["A", "B", "C", "D", "E", "F", "G", "H"],
    #          ["A", "B", "C", "D", "E", "F", "G", "H"]]

    col_values = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}

    king_row = int(king[1])
    king_col_letter = king[0]
    king_col = col_values[king_col_letter]

    queen_row = int(queen[1])
    queen_col_letter = queen[0]
    queen_col = col_values[queen_col_letter]

    if queen_col_letter == king_col_letter or queen_row == king_row:
        return True

    return abs(king_row - queen_row) == abs(king_col - queen_col)


def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    >>> coins(1) == {1, 10}
    True
    >>> coins(2) == {2, 11, 20}
    True
    >>> coins(3) == {3, 12, 21, 30}
    True
    >>> coins(4) == {4, 13, 22, 31, 40}
    True
    >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
    True
    """
    results = set()

    for dimes in range(0, num_coins + 1):
        pennies = num_coins - dimes
        results.add(dimes * 10 + pennies)

    return results


class Node2(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def count_employees(self):
        """Return a count of how many employees this person manages.

        Return a count of how many people that manager manages. This should
        include *everyone* under them, not just people who directly report to
        them.
        """
        count = 0
        for child in self.children:
            count = count + 1 + child.count_employees()

        return count


def dec2bin_back(num):
    """Convert a decimal number to binary representation.
    >>> dec2bin_back(6)
    '110'
    """
    results = []
    place = 0

    while place == 0 or num >= 2**place:

        if num % 2 ** (place + 1):
            num -= 2 ** place
            results.append("1")
        else:
            results.append("0")
        place += 1

    return "".join(reversed(results))


def dec2bin_forward(num):
    """Convert a decimal number to binary representation.
    >>> dec2bin_forward(6)
    '110'
    """
    out = ""
    num_bits = 1

    while 2**num_bits <= num:
        num_bits += 1

    for position in range(num_bits-1, -1, -1):

        if 2**position <= num:
            num -= 2 ** position
            out += "1"
        else:
            out += "0"

    return out


# def hex_convert(hex_in):
#     """Convert a hexadecimal string, like '1A', into it's decimal equivalent.
#     >>> from hexconvert import hex_convert
#     >>> hex_convert('6')
#     6
#     >>> hex_convert('1A')
#     26
#     >>> hex_convert('FFFF')
#     65535
#     """


def largest_sum(nums):
    """Find subsequence with largest sum.
    >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
    [4, -2, 3]
    >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
    [4, -2, 3]
    >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
    [19]
    >>> largest_sum([2, 2, -10, 1, 3, -20])
    [2, 2]
    >>> largest_sum([2, -2, 3, -1])
    [3]
    >>> largest_sum([-1, -2])
    []
    """
    best_sum = 0
    start_best = 0
    end_best = -1

    current_sum = 0
    start_current = 0

    for i, n in enumerate(nums):
        current_sum += n

        if current_sum > best_sum:
            best_sum = current_sum
            start_best = start_current
            end_best = i

        if current_sum <= 0:
            start_current = i + 1
            current_sum = 0

    return nums[start_best:end_best+1]


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
