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


class Node:
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
    board = [["A", "B", "C", "D", "E", "F", "G", "H"],
             ["A", "B", "C", "D", "E", "F", "G", "H"],
             ["A", "B", "C", "D", "E", "F", "G", "H"],
             ["A", "B", "C", "D", "E", "F", "G", "H"],
             ["A", "B", "C", "D", "E", "F", "G", "H"],
             ["A", "B", "C", "D", "E", "F", "G", "H"],
             ["A", "B", "C", "D", "E", "F", "G", "H"],
             ["A", "B", "C", "D", "E", "F", "G", "H"]]


    king_row = king[1]
    king_col = king[0]
    queen_row = queen[1]
    queen_col = queen[0]

    if queen_col == king_col or queen_row == king_row:
        return True

    if king is diagonal:
        up or down a row and back or forward a column
        keep looking through board

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
