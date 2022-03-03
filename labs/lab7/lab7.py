"""
Ethan Kidwell
lab7.py

Problem: Create a program that takes a input file of student grades and
calculated the average based on their weight and percentage and
then writes the results to an output file.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    grade_file = open(in_file_name, 'r')  # remember grades.close()
    average_file = open(out_file_name, 'w')
    # loop through the open file to get grade total for each student
    for line in grade_file:
        name_list = line.split(":")  # splits the list between name and grade
        grades = name_list[1].lstrip()  # removes white space around grades
        grades = grades[0:-1]  # removes new line variable at end of the grades
        grade_list = grades.split(" ")  # splits the grades into their own list

        # converts the grades into integers
        grade_int_list = []
        for val in grade_list:
            grade = int(val)
            grade_int_list.append(grade)

        # loops through to get the total of the weight of each grade
        grade_int_list_len = len(grade_int_list)
        weight_total = 0
        weight_index = 0
        for weight in range(grade_int_list_len // 2):
            weight_total = weight_total + grade_int_list[weight_index]
            weight_index = weight_index + 2

        # allows errors to be explained
        if weight_total < 100:
            name = name_list[0]
            name_w_grade = "{}'s average: {}".format(name, "Error: The weights are less than 100 \n")

            # Write results to the output file
            average_file.write(name_w_grade)

        elif weight_total > 100:
            name = name_list[0]
            name_w_grade = "{}'s average: {}".format(name, "Error: The weights are more than 100 \n")

            # Write results to the output file
            average_file.write(name_w_grade)

        # the actual average calculations
        else:
            # accumulator variables
            w_avg = 0
            weight_index_2 = 0
            grade_index = 1

            # loops through each grade and finds the total plus the weight multiplied together
            for total_grade in range(grade_int_list_len // 2):
                w_avg = w_avg + (grade_int_list[weight_index_2] * grade_int_list[grade_index])
                weight_index_2 = weight_index_2 + 2
                grade_index = grade_index + 2

            # gets the average
            grade_avg = w_avg / 100

            # converts the results into correctly formatted string
            name = name_list[0]
            name_w_grade = "{}'s average: {} \n".format(name, grade_avg)

            # Write results to the output file
            average_file.write(name_w_grade)


def main():
    weighted_average("grades.txt", "avg.txt")
