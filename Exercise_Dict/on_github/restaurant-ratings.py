# your code goes here
import random


def choose_adventure(file_name):
    """Allow user to choose to see ratings in alphabetical order, add a
    new restaurant, or quit"""

    while True:
        user_choice = raw_input("""Would you like to \n
        1. See the restaurant list alphabetically,\n
        2. Add a new restaurant to the list (and see the list), or\n
        3. Update an existing restaurant's rating, \n
        4. Quit?\n
        Enter 1, 2, 3 or 4:\n
        >>>\n """)

        if user_choice == "1":
            sort_restaurant_by_name(file_name, "")
        elif user_choice == "2":
            sort_restaurant_by_name(file_name, "adding_new")
        elif user_choice == "3":
            sort_restaurant_by_name(file_name, "updating_rating")
        elif user_choice == "4":
            return
        else:
            print "You did not choose 1, 2, 3 or 4."


def collect_new_restaurant():
    """Collect new reataurant name and score."""

    user_restaurant = raw_input("What is your favorite restaurant? ").title()

    #try-except to ensure user inputs a number.
    while True:
        try:
            user_restaurant_score = int(raw_input("What is its code? "))
            break
        except Exception:
            print "Please enter a number between 1 - 5."

    return user_restaurant, user_restaurant_score


def updating_restaurant(dic):
    """Updating a random restaurant rating score"""
    updating_option = raw_input("""Would you like to:\n
    1. Choose the restaurant to update, or \n
    2. Let us choose a random one?\n
    Please enter 1 or 2:  >>> \n""")

    if updating_option == "1":
        restaurant_name = raw_input("""Options: Big Bean Shack, Chip shop, Diagon Alley cafe,
            Eternelle's Elixir of Refreshment, Florean Fortescue's Ice Cream Parlour, Jellied Eel Shop,
            Luchino Caffe, Ministry Munchies, The Bear & Staff, The Club, The Porcupine, or The Tavern.
            Restaurant name: """)
        restaurant_rating = dic[restaurant_name]

    else:
        restaurant_name = random.choice(dic.keys())
        restaurant_rating = dic[restaurant_name]

    print "The random restaurant is %s and its rating score is %s" % (restaurant_name, restaurant_rating)

    while True:
        try:
            new_rating = int(raw_input("What is the new rating? "))
            break
        except Exception:
            print "Please enter a number between 1 - 5."

    dic[restaurant_name] = new_rating

    return dic


def sort_restaurant_by_name(file_name, options):
    """Create dictionary and modify the dictionary accordig to user chosen option."""

    the_file = open(file_name)

    dic = {}

    for line in the_file:
        key, value = line.rstrip().split(":")
        dic[key] = value

    if options == "adding_new":
        user_restaurant, user_restaurant_score = collect_new_restaurant()
        dic[user_restaurant] = user_restaurant_score

    if options == "updating_rating":
        dic = updating_restaurant(dic)

    sorted_key = sorted(dic)

    for restaurant in sorted_key:
        print restaurant + " is rated at " + str(dic[restaurant])

choose_adventure("scores.txt")
