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

filename = sys.argv[1]

words = find_words(filename)

get_user_rating()

sorted_rest = sort_by_rest(words)

print_rest_rating(sorted_rest)
