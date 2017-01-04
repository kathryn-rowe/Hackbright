#Import Statements
import random

#Getting user name
print("Hello!")
name = raw_input("What is your name: ")

#Added replay variable to allow for replayble game
replay = True

#Added score variable to record high scores
score = None

#While loop to enclose game mechanics
while replay:
    print("%s, I'm thinking of a number between 1 and 100.") % name
    print("Try to guess my number.")

    #Genertaing random number and setting base value for guess and num_guess
    number = random.randint(1, 100)
    guess = None
    num_guess = 0

    #While loop to enclose guessing section of game
    while number != guess:

        #Using try/except to catch non-numbers
        try:

            #Prompting for guess and giving hint based on value
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

    #If statement to check for new high score
    if num_guess < score or score is None:
        score = num_guess
        print("NEW HIGH SCORE!!!!!!")

    print("Congratulations, your best score is %d!") % score

    answer = raw_input("Would you like to play again? (Y/N) ")
    if answer == "N":
        replay = False
