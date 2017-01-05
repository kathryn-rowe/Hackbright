"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

def parse_expression():
    while True:
        expression = raw_input("> ")
        tokens = expression.split(" ")
    #    print tokens
    #    print len(tokens)

        first_token = tokens[0]

        if first_token == 'q':
            return

        if len(tokens) == 3:

            first_number = int(tokens[1])
            second_number = int(tokens[2])

            if first_token == "+":
                print add(first_number, second_number)
            elif first_token == "-":
                print subtract(first_number, second_number)
            elif first_token == "*":
                print multiply(first_number, second_number)
            elif first_token == "/":
                print divide(first_number, second_number)
            elif first_token == "square":
                print square(first_number, second_number)
            elif first_token == "cube":
                print cube(first_number, second_number)
            elif first_token == "pow":
                print power(first_number, second_number)
            elif first_token == "mod":
                print mod(first_number, second_number)
            else:
                print "That is not a valid operator!"
        else:
            print "That was not a valid input."

parse_expression()
