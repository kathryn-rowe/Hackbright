def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called "houses" that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army"
            ])

    """
    houses = set()
    for row in open(filename):
        row = row.rstrip()
        row = row.split("|")
        if row[2] != '':
            houses.add(row[2])

    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort, skipping instructors.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name. Puts ghosts into a separate list entitled "ghosts".
    Returns a list of these lists.

        ex. fall_15 = ["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ""Hermione Granger", ... ]
        ex. all_students = [["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ...],
        ["Lee Jordan", "Andrew Kirke", "Neville Longbottom", ...],
        ["Cormac McLaggen", "Parvati Patil", "Jimmy Peakes", ...],
        ["Euan Abercrombie", "Katie Bell", "Lavender Brown", ...]]

    """

    all_students = []
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    for row in open(filename):
        row = row.rstrip()
        row = row.split("|")
        if row[0] != '' or row[1] != '':
            student_name = row[0] + " " + row[1]

            if row[4] == "Winter 2016":
                winter_16.append(student_name)
            elif row[4] == "Spring 2016":
                spring_16.append(student_name)
            elif row[4] == "Summer 2016":
                summer_16.append(student_name)
            elif row[4] == "Fall 2015":
                fall_15.append(student_name)
            elif row[4] == "G":
                ghosts.append(student_name)

    all_students.append(winter_16)
    all_students.append(spring_16)
    all_students.append(summer_16)
    all_students.append(fall_15)
    all_students.append(ghosts)

    for cohort in all_students:
        cohort.sort()

    return all_students


def hogwarts_by_house(filename):
    """TODO: Sort students by house.


    Iterates over the data to create a list for each house, and sorts students
    into their appropriate houses by last name. Sorts ghosts into a list called "ghosts"
    and instructors into a list called "instructors".
    Returns all lists in one list of lists.

        ex. gryffindor = ["Abercrombie", "Bell", "..." ]
        ex. ghosts = ["Baron", "Friar", "..."]
        ex. all_students = [ hufflepuff,
                    gryffindor,
                    ravenclaw,
                    slytherin,
                    dumbledores_army,
                    ghosts,
                    instructors
        ]

    """

    all_hogwarts = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    ravenclaw = []
    ghosts = []
    instructors = []

    for row in open(filename):
        row = row.rstrip()
        row = row.split("|")

        first, last, house, instructor, cohort = row

        if row[2] == "Gryffindor":
            gryffindor.append(last)
        elif row[2] == "Hufflepuff":
            hufflepuff.append(last)
        elif row[2] == "Slytherin":
            slytherin.append(last)
        elif row[2] == "Dumbledore's Army":
            dumbledores_army.append(last)
        elif row[2] == "Ravenclaw":
            ravenclaw.append(last)
        elif row[-1] == "I":
            instructors.append(instructor)
        elif row[-1] == "G":
            ghosts.append(last)

    all_hogwarts.append(gryffindor)
    all_hogwarts.append(hufflepuff)
    all_hogwarts.append(slytherin)
    all_hogwarts.append(dumbledores_army)
    all_hogwarts.append(ravenclaw)
    all_hogwarts.append(ghosts)
    all_hogwarts.append(instructors)

    for sector in all_hogwarts:
        sector.sort()

    return all_hogwarts


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. student_list = [
                ("Euan Abercrombie", "Gryffindor", "McGonagall", "Summer 2016"),
                ("Katie Bell", "Gryffindor", "McGonagall", "Summer 2016"),
                # ...
            ]
    """

    student_list = []

    for row in open(filename):
        row = row.rstrip()
        row = row.split("|")

        first, last, house, instructor, cohort = row

        if house:
            student_list.append((first + " " + last, house, instructor, cohort))

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Uses the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name from the command line, returns that
    student's cohort, or returns "Student not found." when appropriate. """

    user_input = raw_input("Who are you looking for? >>")

    for student in student_list:
        name, house, instructor, cohort = student
        if name.lower() == user_input.lower():
            print "Yes, I found %s in my student list. They were in cohort %s." % (name, cohort)
            return cohort
        else:
            print "Unable to find that student."
            return "Student not found"


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student last names that have duplicates.

    Iterates over the data to find any last names that exist across all cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Weasley"])

    """

    duplicate_names = set()

    fall_15 = set()
    winter_16 = set()
    spring_16 = set()
    summer_16 = set()

    for row in open(filename):
        row = row.rstrip()
        student = row.split("|")

        first_name, last_name, house, instructor, cohort = student

        if cohort == "Fall 2015":
            fall_15.add(last_name)
        elif cohort == "Winter 2016":
            winter_16.add(last_name)
        elif cohort == "Spring 2016":
            spring_16.add(last_name)
        elif cohort == "Summer 2016":
            summer_16.add(last_name)

    duplicate_names = fall_15 & winter_16 & spring_16 & summer_16

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and when given a name, print a statement of everyone in their house in their cohort.

    Uses the list of tuples generated by all_students_tuple_list to make a small function
    that, when given a student's first and last name, print students that are in both
    that student's cohort and that student"s house.

    ex: Choose a student: Hermione Granger
        Hermione Granger was in house Gryffindor in the Fall 2015
        cohort.
        The following students are also in their house:
        Seamus Finnigan
        Angelina Johnson
        Harry Potter
        Ron Weasley
        Oliver Wood


    """

    user_choice = raw_input("Which name should I search for? (first and last name, ex. Hermione Granger) >>")

    for student in student_list:
        name, house, instructor, cohort = student
        if user_choice.lower() == name.lower():
            print "%s was in house %s in the %s cohort" % (name, house, cohort)
            print "The following students are also in their house:"

            for other_students in student_list:
                if other_students[3] == cohort and other_students[0] != name and other_students[1] == house:
                    print other_students[0]
            return

    print "Could not find that student."



#########################################################################################

# Here is some useful code to run these functions!

print unique_houses("cohort_data.txt")
print sort_by_cohort("cohort_data.txt")
print hogwarts_by_house("cohort_data.txt")
all_students_data = all_students_tuple_list("cohort_data.txt")
print all_students_data
find_cohort_by_student_name(all_students_data)
print find_name_duplicates("cohort_data.txt")
find_house_members_by_student_name(all_students_data)