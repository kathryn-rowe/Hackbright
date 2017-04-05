import sys

rest_rating = {}


def find_words(filename):
    """Reads restaurant name and rating from file, returns a dictionary of name:rating pair"""

    for line in open(filename):
        restaurant, rating = line.rstrip().split(":")
        rest_rating[restaurant] = rating

    return rest_rating


def get_user_rating():
    """Prompt user for restaurant and rating score. Add to dictionary"""

    user_restaurant = raw_input("Which restaurant would you like to rate? >> ")
    user_rating = raw_input("And what score would you give that restaurant? (1=bad, 5=great) >> ")

    rest_rating[user_restaurant] = user_rating


def sort_by_rest(rest_rating):
    """Reads restaurant, rating pair, sorts alphebetically by restaurant"""

    return sorted(rest_rating.iteritems())


def print_rest_rating(rest_rating):
    """Prints restaurant, rating pair"""

    for restaurant, rating in rest_rating:
        print restaurant + " " + str(rating)


def get_user_choice():
    """Gets user's choice of whether to 1) seeing all the ratings (in alphabetical order),
                                        2) adding a new restaurant (and rating it), or
                                        3) quitting."""

    user_choice = str(raw_input("Would you like to 1) see all the ratings (in alphabetical order), 2) add a new restaurant (and rating it), or 3) quit? >> "))

    if user_choice == "1":
        print_rest_rating(sorted_rest)
        get_user_choice()
    elif user_choice == "2":
        get_user_rating()
    else:
        return

filename = sys.argv[1]

words = find_words(filename)

sorted_rest = sort_by_rest(words)

get_user_choice()
