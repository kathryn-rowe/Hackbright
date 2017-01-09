def all_odd(numbers):
    """Return a list of only the odd numbers in the input list."""

    odd_numbers = []
    #create an empty string

    for each_number in numbers:
        if each_number % 2 == 1:
            odd_numbers.append(each_number)

    return odd_numbers


def print_indices(items):
    """Print index of each item in list, followed by item itself."""

    for index, item in enumerate(items):
        print index, item


def foods_in_common(foods1, foods2):
    """Find foods in common between to lists and return in alphebetical list."""

    set_foods2 = set(foods2)
    set_foods1 = set(foods1)
    #create sets for each list in order to set-math!

    foods_in_common_set = set_foods1 & set_foods2
    #combines the two sets and find cominality

    if len(foods_in_common_set) > 0:
        foods_in_common_list = list(foods_in_common_set)
    else:
        return []
        #if there aren't any arguments passed, return empty list per instructions.

    return sorted(foods_in_common_list)


def every_other_item(items):
    """Return every other item in `items`, starting at first item."""

    every_other_item_list = []
    #create empty list

    for each_item in items[::2]:
        #iterate through list by two using list slicing. Add to new list.
        every_other_item_list.append(each_item)

    return every_other_item_list


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order."""

    ascending_order = sorted(items)
    #sort in ascending order the list passed as an argument.

    if n != 0:
        largest_n_items = ascending_order[-n:]
        return largest_n_items
        #iterate through ascending order list and take the nth largest numbers from the right.
    else:
        return []

#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
