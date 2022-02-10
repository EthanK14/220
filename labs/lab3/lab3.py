"""
Ethan Kidwell
lab3.py

Problem: To get the average number of cars on a specified amount of roads and days the counters were active,
then take all this and find average number of cars be road and then the total of cars and average of all the roads.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def traffic():
    roads_surveyed = eval(input("How many roads were surveyed? "))
    total_cars = 0
    # Accumulator variable to find the total number of cars
    for roads in range(roads_surveyed):  # takes the number of roads enter and makes it loop that many times
        cars = 0
        # Accumulator variable to find the total number of cars per road
        print("How many days was road", roads + 1, "surveyed?")
        days_surveyed = eval(input(" "))
        # allows the user to input how many days the road was surveyed
        for days in range(days_surveyed):
            print("How many cars cars traveled on day ", days + 1)
            car_traveled = eval(input(" "))
            # allows the user to input how many cars traveled that road that day
            cars = cars + car_traveled
            # Accumulates the number the cars per day to the cars variable
            total_cars = total_cars + car_traveled
            # Accumulating the total number of cars per day to gather sum of all the cars on all roads
        avg_cars = cars / days_surveyed
        # Calculates the average of cars per day
        print("Road", roads + 1, "averages", avg_cars, "vehicles per day: ")
        # Prints the average of cars per road
    print("The total number of cars is ", total_cars)
    avg_total_cars = total_cars / roads_surveyed
    # Calculating the average number of cars per the number of roads
    print("Average number of cars per road:", avg_total_cars)


traffic()
