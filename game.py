# Put your code here
import random
print("Hello!")
name = raw_input("What is your name: ")
print("%s, I'm thinking of a number between 1 and 100.") % name
print("Try to guess my number.")
number = random.randint(1, 100)
guess = None
num_guess = 0

while number != guess:
    guess = raw_input("What is your guess: ")
    num_guess += 1
    if guess > number:
        print "Your guess is too high. Try again."
    if guess < number:
        print "Your guess is too low. Try again"

print("Well done, %s! You found my number in %d tries.") % (name, num_guess)
