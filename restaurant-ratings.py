# your code goes here
def sort_restaurant_by_name(file_name):
    """Sort restaurant by name"""

    the_file = open(file_name)

    dic = {}

    for line in the_file:
        key, value = line.rstrip().split(":")
        dic[key] = value

    user_restaurant = raw_input("What is your favorite restaurant? ")
    user_restaurant_score = int(raw_input("What is its code? "))

    dic[user_restaurant] = user_restaurant_score

    sorted_key = sorted(dic)

    for restaurant in sorted_key:
        print restaurant + " is rated at " + str(dic[key])

sort_restaurant_by_name("scores.txt")
