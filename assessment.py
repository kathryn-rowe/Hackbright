# PART ONE


def is_hometown(town_name):
    """Evaluates if the name of the town given is my hometown, Luck.


    If the argument is Luck, then it is true. If it is not Luck, then it is false"""

    if str(town_name) == "Luck" or str(town_name) == "luck":
        #made the input town_name a string in case someone adds a number.
        return True
    else:
        return False
        #could also have a print statement say 'this isn't Kate's hometown'


def combine_first_last_name(first_name, last_name):
    """Takes two names, first and last, as arguments and returns them together
    as one string. """

    return str(first_name) + " " + str(last_name)
    #added the string function in case someone has a number in their name.


def learn_persons_name_hometown(hometown, first_name, last_name):
    """Finding the hometown, first name and last name of someone.

    Combine all these attributes, call previous functions ()"""

    name_combine = combine_first_last_name(first_name, last_name)
    #takes information from previously created function creating the combo of
    #input first and last names. This variable makes the if statement cleaner below.

    if is_hometown(hometown):
        #finds if the function returns to True, therefore same hometown
        print "Hi, " + name_combine + ", we're from the same place!"
    else:
        print "Hi, " + name_combine + ", where are you from?"



###############################################################################

# PART TWO


def is_berry(fruit):
    """Determines if fruit is a berry"""

    fruit_lower = fruit.lower()
    #this was something extra I added to make sure the input argument will return
    #true if the correct berry was input into the statement below, regardless of cases.

    if fruit_lower == "strawberry" or fruit_lower == "cherry" or fruit_lower == "blackberry":
        return True
    else:
        return False


def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    if is_berry(fruit) is True:
        return 0
    else:
        return 5


def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    new_list = []
    #create empty list to add values. New_list isn't very creative, but it is direct.

    for number in lst:
        #again, variables aren't very creative but they make sense and are better
        #than x,y or banana.
        new_list.append(number)

    new_list.append(num)

    return new_list


def calculate_price(item_price, state_abbrev, tax_percent=0.05):
    """Calculate the total amount of an item after applicable taxes and fees
    are applied.

    Find tax by multipling rate to the item price and then adding that amount
    to the item price. Find the fee by state abbreviation. Each state has its
    own fee codes. Function below uses fee examples given in directions. Total
    calculated price includes tax and state fee.

    Correct tax rates are dependent on argument input. If I was to continue
    writing this code, I would find a text document of all state codes and
    open file, loop through records, and input correct values. Right now I have
    no way of knowing (other than looking for each state rate online) if the user
    input is correct and if the default of 5%  applies to states. """

    if state_abbrev == "CA" or state_abbrev == "ca":
    #CALIFORNIA: state abbreviation is suppose to be a two-letter input.
    #Could include a try-except statement to catch inputs longer than two letters.

        ca_fee = .03

        if tax_percent != .05:
            #find the price with tax, then multiple by CA's 3% fee
            price_with_tax = (item_price * (tax_percent / 100)) + item_price
            total_price = (price_with_tax * ca_fee) + price_with_tax
            return round(total_price, 1)
            #rounded values to not have more than 2 decimal points.
        else:
            price_with_tax = ((item_price * .05) + item_price)
            total_price = (price_with_tax * ca_fee) + price_with_tax
            return round(total_price, 1)
            #rounded values to not have more than 2 decimal points.

    elif state_abbrev == "PA" or state_abbrev == "pa":
    #PENNSYLVANIA: state abbreviation is suppose to be a two-letter input.
    #Could include a try-except statement to catch inputs longer than two letters.

        pa_fee = 2.0

        if tax_percent != 0.05:
            price_with_tax = (item_price * (tax_percent / 100)) + item_price
            total_price = price_with_tax + pa_fee
            return round(total_price, 1)
            #rounded values to not have more than 2 decimal points.

        else:
            #if the tax argument is forgetten, 5% is calculated.
            total_price = ((item_price * 0.05) + item_price) + pa_fee
            return round(total_price, 1)
            #rounded values to not have more than 2 decimal points.

    elif state_abbrev == "MA" or state_abbrev == "ma":
    #MASSACHUSETTS: state abbreviation is suppose to be a two-letter input.
    #Could include a try-except statement to catch inputs longer than two letters.

        if item_price < 100:
            #MA fee depends on if item is more or less than $100

            ma_fee_less_100 = 1.0

            if tax_percent != 0.05:
                price_with_tax = (item_price * (tax_percent / 100)) + item_price
                total_price = price_with_tax + ma_fee_less_100
                return round(total_price, 1)
                #rounded values to not have more than 2 decimal points.

            else:
                #if the tax argument is forgetten, 5% is calculated.
                total_price = ((item_price * 0.05) + item_price) + ma_fee_less_100
                return round(total_price, 1)
                #rounded values to not have more than 2 decimal points.
        else:

            ma_fee_more_100 = 3.0

            if tax_percent != 0.05:
                price_with_tax = (item_price * (tax_percent / 100)) + item_price
                total_price = price_with_tax + ma_fee_more_100
                return round(total_price, 1)
                #rounded values to not have more than 2 decimal points.

            else:
                #if the tax argument is forgetten, 5% is calculated.
                total_price = ((item_price * 0.05) + item_price) + ma_fee_more_100
                return round(total_price, 1)
                #rounded values to not have more than 2 decimal points.

    else:
        #to find total price of item in states other than CA, PA, MA
        if tax_percent != 0.05:
            price_with_tax = (item_price * (tax_percent / 100)) + item_price
            return price_with_tax

        else:
            total_price = (item_price * 0.05) + item_price
            return round(total_price, 1)
            #rounded values to not have more than 2 decimal points.

###############################################################################

# PART THREE: ADVANCED


def append_arguments_to_list(input_list, *args):
    """This function takes in a list and any number of additional number of
    arguments, appends them to the list, and returns the entire list."""

    #create empty list to put in arguments
    new_list = []

    for item in input_list:
        #iterate of the list given and add them to the empty list.
        new_list.append(item)
    for argument in args:
        #iterate over the unknown amount of arguments and add each one to the new list.
        new_list.append(argument)
    return new_list


def get_word(word):
    """Function gets word as argument"""

    def mult_by_three(argument):
        """Multiples argument by 3, no spacing"""

        return str(argument) * 3
        #made the argument a string in case a number is added, therefore the output
        #would be a value/one number

    #returns the word used as the argument and a non-spaced version of that word.
    return word, mult_by_three(word)

###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
