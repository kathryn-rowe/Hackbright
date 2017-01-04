# Put your code here
import random
print("Hello!")
name = raw_input("What is your name: ")
print("%s, I'm thinking of a number between 1 and 100.") % name
print("Try to guess my number.")
number = random.randint(1, 100)
print number
guess = None
num_guess = 0

while number != guess:
    try:
        guess = int(raw_input("What is your guess: "))
        num_guess += 1
        if (guess > 100 or guess < 1):
            print "Your number is not what we asked for! Shame!"
        elif guess > number:
            print "Your guess is too high. Try again."
        elif guess < number:
            print "Your guess is too low. Try again"
    except:
        print "That's not even a number. Dishonor on you!"

print("Well done, %s! You found my number in %d tries.") % (name, num_guess)
