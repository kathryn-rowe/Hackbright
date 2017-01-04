# Put your code here
import random
print("Hello!")
name = raw_input("What is your name: ")
reply = True
score = 100
while reply:
    print("%s, I'm thinking of a number between 1 and 100.") % name
    print("Try to guess my number.")
    number = random.randint(1, 100)
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

    if num_guess < score:
        score = num_guess
        print("NEW HIGH SCORE!!!!!!")
    print("Congratulations, your best score is %d!") % score
    answer = raw_input("Would you like to play again? (Y/N) ")
    if answer == "N":
        reply = False
