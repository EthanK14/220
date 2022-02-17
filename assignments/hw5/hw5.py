"""
Name: Ethan Kidwell
hw5.py

Problem: To print a name from first, last to last, first, to split a domain name,
to print the initials of a specified number of students, print the initials of a list of names
entered from the user, ask a user the number of sentences to input and
then get the sentences and then output every third character in the sentences,
take a sentence and calculate the average word length, and a function that takes
sentences and stories and moves the first letter to the end of the word and follows with ay.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("Enter a name (first last):")  # takes name from user
    name_input = name.split(' ')  # splits name into a list

    # adds the first and last name to a new list but in a reverse order
    last_name = [name_input[1], name_input[0]]

    # joins the new formatted list into a string separated by a comma
    name_form = ', '.join(last_name)
    print(name_form)


def company_name():
    domain_name = input("Enter a domain name:")
    print(domain_name[4:-4])  # excludes first four and last four characters


def initials():
    num_students = eval(input("How many students are in the class?"))
    for i in range(num_students):
        student_name = input("What is the name of the student?")
        first_initial = student_name[0]
        space = student_name.find(" ")
        last_initial = space + 1
        print(first_initial + student_name[last_initial])


def names():
    name = input("Enter a list of names: ")  # gets the list of names
    name_list = name.split(', ')  # creates that into a list
    initial_list = []  # accumulator variable for initials
    # loop to get all initals from name list
    for first_last in name_list:
        full_name = first_last  # sets the name to string value
        space = full_name.rfind(" ")  # finds the last name index value
        first_initial = full_name[0]  # gets the first initial
        last_initial = full_name[space + 1]  # gets the last initial
        initial_final = first_initial + last_initial  # adds the first and last initial together
        initial_list.append(initial_final)  # adds the initial to accumulator list
    print(initial_list)




def thirds():
    pass


def word_average():
    pass


def pig_latin():
    pass


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
