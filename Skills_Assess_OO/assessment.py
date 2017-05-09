"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   a. Encapsulation: If we call a certain class, we get all its similar-type capabilities
   within that class. We also do not have to use all its functionality, but it is available
   in one package.

   b. Polymorphism: When applied to classes, Polymorphism refers to the flexibility of
   a class and applying its functionality to different applications. It can reduce repeated
   code.

   c. Abstraction: This idea has to deal with the fact that you don't have to know
   everything that is happening within a class. You can trust that the class will
   work (provide you with an appropriate output) and you can incorporate it into your
   own code. It hides the complexity.

2. What is a class?
   It is a structured, flexible, designed "blueprint." You can create different types of
   objects from this blueprint.

3. What is an instance attribute?
   Similar to a variable, but it is a singular occurance of a identifier/value pairing;
   the "post-it" on an object.
   Classes look at the instance attribute first when looking for a value.

4. What is a method?
   Similar to a method, but found within a class. They can perform an operation.

5. What is an instance in object orientation?
   A unique or singular value - attribute connection within a class. It refers to
   one "thing" and does not define value for a group of other "things."

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute can apply a characteristic/value to a group of items found
   within that class. A instance is singular, or individual. If you have a class
   of clouds, I would say they all have a class attribute of being made from water.
   A fog clould would have an instance attribute of being close to the earth.


"""


class Student(object):
    """Creates a student with address"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        student_dict = {}
        student_dict["first_name"] = first_name
        student_dict["last_name"] = last_name
        student_dict["address"] = address


class Question(object):
    """Stores questions and prints/evaluates answer"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        question_dict = {}
        question_dict["question"] = question
        question_dict["correct_answer"] = correct_answer

    def ask_and_evaluate(self):
        """Prints questions and gets answer from user"""

        print self.question
        answer = raw_input()
        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(Question):
    """Initiates exam and collects score"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Adds a question to the list of questions"""

        super(add_question, self).__init__(question, correct_answer)

    def administer(self):
        score = 0
        for question, answer in self.question_dict.items():
            self.ask_and_evaluate()
            if self.ask_and_evaluate() is True:
                score += 1.0
        print score

question = Question("What's this", "Answer")

question.ask_and_evaluate()

def take_test(exam, student):
    exam = Exam.administer()

def example():
    midterm = Exam("Midterm")
    midterm.add_question("What is the color of the sky?", "blue")
    student = Student("Jane", "Smith", "101 North Hwy")
    Exam.administer()
