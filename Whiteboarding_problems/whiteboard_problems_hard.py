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


def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent.
    >>> hex_convert('6')
    6
    >>> hex_convert('1A')
    26
    >>> hex_convert('FFFF')
    65535
    """
    letter_val = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    total = 0
    hex_val = 1

    for char in hex_in[-1::-1]:
        if char in letter_val:
            total += hex_val * letter_val[char]
        else:
            total += hex_val * int(char)
        hex_val *= 16

    return total


def find_carrots(four_cells, nrows, ncols, garden):

    cell_lst = [(row, col) for row, col in four_cells
                if 0 <= row < nrows and 0 <= col < ncols]

    num_carrots = 0
    best = None

    for row, col in cell_lst:
        # print row, col
        if num_carrots < garden[row][col]:
            best = row, col
            num_carrots = garden[row][col]
    return best


def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten.
    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]
    >>> lunch_count(garden)
    15
    """

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(type(c) is int for c in row for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])

    four_cells = [(((nrows - 1) / 2), ((ncols - 1) / 2)),
                  (((nrows - 1) / 2), ((ncols - 0) / 2)),
                  (((nrows - 0) / 2), ((ncols - 1) / 2)),
                  (((nrows - 0) / 2), ((ncols - 0) / 2))]

    eaten = 0

    while True:

        current = find_carrots(four_cells, nrows, ncols, garden)

        if not current:
            return eaten

        row, col = current

        eaten += garden[row][col]

        garden[row][col] = 0

        four_cells = [(row, col-1), (row - 1, col), (row, col + 1), (row + 1, col)]


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


class DLLNode(object):
    """Doubly-linked node."""

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return "<Node prev=%s data=%s next=%s>" % (
            self.prev.data, self.data, self.next.data)

    @classmethod
    def make_list(cls, num):

        first = node = prev = cls(1)

        # Make all other nodes
        for i in range(2, num + 1):
            node = DLLNode(i, prev=prev)
            prev.next = node
            prev = node

        # Fix the last and first node's prev/next
        node.next = first
        first.prev = node

        return first


def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor.
    >>> find_survivor(10, 3)
    4
    """
    node = DLLNode.make_list(num_people)

    while node.next != node:
        # get to the third node
        for i in range(kill_every - 1):
            node = node.next
        # when you get to the third node, kill it
        node.prev.next = node.next
        node.next.prev = node.prev

        node = node.next

    return node. data


def primes(count):
    """Return count number of prime numbers, starting at 2.
    >>> primes(1)
    [2]
    >>> primes(5)
    [2, 3, 5, 7, 11]
    """
    def _is_prime(num):
        if num < 2:
            return False

        if num == 2:
            return True

        if num % 2 == 0:
            return False

        n = 3

        while n * n <= num:
            if num % n == 0:
                return False
            n += 2
        return True

    primes = [2]
    num = 3

    while len(primes) < count:
        if _is_prime(num):
            primes.append(num)
        num += 1

    return primes


def rev(s):
    """Reverse word-order in string, preserving spaces.
    >>> rev("")
    ''
    >>> rev("hello")
    'hello'
    >>> rev("hello world")
    'world hello'
    >>> rev(" hello  world   ")
    '   world  hello '
    """
    in_space = None
    tokens = []
    current_token = ''

    for letter in s:
        if letter == " ":
            if not in_space:
                tokens.append(current_token)
                current_token = ''
                in_space = True
        else:
            if in_space:
                tokens.append(current_token)
                current_token = ''
                in_space = False
        current_token += letter
    tokens.append(current_token)

    return "".join(reversed(tokens))


class Node5(object):
    """Doubly-linked node in a tree.
        >>> na = Node5("na")
        >>> nb1 = Node5("nb1")
        >>> nb2 = Node5("nb2")
        >>> nb1.set_parent(na)
        >>> nb2.set_parent(na)
        >>> na.children
        [<Node nb1>, <Node nb2>]
        >>> nb1.parent
        <Node na>
    """
    parent = None

    def __init__(self, data):
        self.children = []
        self.data = data

    def __repr__(self):
        return "<Node %s>" % self.data

    def set_parent(self, parent):
        """Set parent of this node.
        Also sets the children of the parent to include this node.
        """
        self.parent = parent
        parent.children.append(self)

    def siblings(self):
        """Find nodes on the same level as this node.
        >>> b.cousins() == {c, d}
        True
        >>> c.cousins() == {b, d}
        True
        >>> e.cousins() == {f, g, h, i, j}
        True
        >>> k.cousins() == {l}
        True
        >>> a.cousins() == set()
        True
        """
        if self.parent is not None:
            parent = self.parent
            kids = parent.children
        siblings = set()

        for kid in kids:
            if self.data != kid:
                siblings.add(kid)

        return siblings


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
