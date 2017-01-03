# Put your code here
import random
print("Hello!")
name = raw_input("What is your name: ")
print("%s, I'm thinking of a number between 1 and 100.") % name
print("Try to guess my number.")
number = random.randint(1,100)
guess = None
too_high = 101
too_low = 0

while number != guess:
    guess = (too_high-too_low)/2 + too_low
    print guess
    guess= number
    