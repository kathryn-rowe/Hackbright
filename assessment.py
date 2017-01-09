"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.


def is_hometown(town_name):
    """Evaluates if the name of the town given is my hometown, Luck.


    If the argument is Luck, then it is true. If it is not Luck, then it is false"""

    if town_name == "Luck" or town_name == "luck":
        return True
    else:
        return False


#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.


def combine_first_last_name(first_name, last_name):
    """Takes two names, first and last, as arguments and returns them together
    as one string. """

    print str(first_name) + " " + str(last_name)
    #added the string function in case someone has a number in their name.


#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.


def learn_persons_name_hometown(hometown, first_name, last_name):
    """Finding the hometown, first name and last name of someone.

    Combine all these attributes, call previous functions ()"""


###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""

    if fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry":
        return True
    else:
        return False


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    if is_berry(fruit) is True:
        return 0
    else:
        return 5



# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.


def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    new_list = []
    for number in lst:
        new_list.append(number)

    new_list.append(num)

    return new_list



# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.


def calculate_price(item_price, state_abbrev, tax_percent=0.05):
    """Calculate the total amount of an item after applicable taxes and fees
    are applied.

    Find tax by multipling rate to the item price and then adding that amount
    to the item price. Find the fee by state abbreviation. Each state has its
    own fee codes. Function below uses fee examples given in directions. Total
    calculated price includes tax and state fee."""

    if state_abbrev == "CA" or state_abbrev == "ca":
    #state abbreviation is suppose to be a two-letter input. Could include a
    #try-except statement to catch inputs longer than two letters.

        ca_fee = .03

        if tax_percent != .05:
            price_with_tax = (item_price * (tax_percent / 100)) + item_price
            total_price = (price_with_tax * ca_fee) + price_with_tax
            return round(total_price, 1)
        else:
            price_with_tax = ((item_price * .05) + item_price)
            total_price = (price_with_tax * ca_fee) + price_with_tax
            return round(total_price, 1)

    elif state_abbrev == "PA" or state_abbrev == "pa":
    #state abbreviation is suppose to be a two-letter input. Could include a
    #try-except statement to catch inputs longer than two letters.

        pa_fee = 2.0

        if tax_percent != 0.05:
            price_with_tax = (item_price * (tax_percent / 100)) + item_price
            total_price = price_with_tax + pa_fee
            return round(total_price, 1)
        else:
            total_price = ((item_price * 0.05) + item_price) + pa_fee
            return round(total_price, 1)

    elif state_abbrev == "MA" or state_abbrev == "ma":
    #state abbreviation is suppose to be a two-letter input. Could include a
    #try-except statement to catch inputs longer than two letters.

        if item_price < 100:
            ma_fee_less_100 = 1.0
            if tax_percent != 0.05:
                price_with_tax = (item_price * (tax_percent / 100)) + item_price
                total_price = price_with_tax + ma_fee_less_100
                return round(total_price, 1)
            else:
                total_price = ((item_price * 0.05) + item_price) + ma_fee_less_100
                return round(total_price, 1)
        else:
            ma_fee_more_100 = 3.0
            if tax_percent != 0.05:
                price_with_tax = (item_price * (tax_percent / 100)) + item_price
                total_price = price_with_tax + ma_fee_more_100
                return round(total_price, 1)
            else:
                total_price = ((item_price * 0.05) + item_price) + ma_fee_more_100
                return round(total_price, 1)
    else:
        if tax_percent != 0.05:
            price_with_tax = (item_price * (tax_percent / 100)) + item_price
            return price_with_tax
        else:
            total_price = (item_price * 0.05) + item_price
            return round(total_price, 1)

###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.


# def append_arguments_to_list(input_list, ):
#     new_list = []

# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


# def nested_function(inner_function()):


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
