"""
Name: Ethan Kidwell

Problem: Encapsulates the data for sales person

Certificate of Authenticity
I certify that the work is entirely my own.
"""
from sales_person import SalesPerson


class SalesForce:
    """
    Creates a list of employees
    """

    def __init__(self):
        """
        Creates an empty list to put the employee in
        """
        self.sales_people = []

    def add_data(self, file_name):
        """
        Imports data from a file with the information of sales people and
        adds it all into a list
        """
        employee_file = open(file_name, 'r')
        for employee in employee_file.readlines():
            self.sales_people.append(employee[:-1])

    def __add_employee(self):
        """
        edits the sales_people list and takes each employee adds them to a list within the
        sales_people list. Then takes and splits their id #, name into their own elements
        and takes their sales and splits them into their own list within the employee's
        list. it then takes all this data and adds it all of it to create and return a list
        of employee objects.
        """
        employee_list = []
        # loops through list of sales people
        for num in range(len(self.sales_people)):  # loops through the first element of the list
            self.sales_people[num] = [self.sales_people[num]]  # adds that element to a list within the list
            # splits the name and id and sales into their own elements
            self.sales_people[num] = self.sales_people[num][0].split(', ')
            # splits all the sales into their own elements
            self.sales_people[num][2] = self.sales_people[num][2].split(' ')
            # creates them all as employee objects
            employee = SalesPerson(self.sales_people[num][0], self.sales_people[num][1])
            acc = 2  # accumulates to ensure all sales are added
            acc_2 = 0
            for sale in range(len(self.sales_people[num][2])):
                employee.enter_sale(self.sales_people[num][2][acc_2])  # adds sales to employee object
                acc = acc + 1
                acc_2 = acc_2 + 1
            employee_list.append(employee)
        return employee_list

    def quota_report(self, quota):
        """
        Returns a list where each element is the sellers' employee id
        name, total sales, and a boolean value if the hit the quota value given
        """
        employee_list = []
        # loops through list of sales people
        for employee in self.__add_employee():  # loops through the first element of the list
            employee_total = employee.total_sales()
            if employee_total >= quota:
                employee_name = [employee.get_id(), employee.get_name(), True]
                employee_list.append(employee_name)
            elif employee_total < quota:
                employee_not = [employee.get_id(), employee.get_name(), False]
                employee_list.append(employee_not)
        return employee_list

    def top_seller(self):
        """
        returns a list of the top most seller and in the case of a tie it should
        return all those with that value
        """
        pass

    def individual_sales(self, employee_id):
        """
        Returns the sales of the given id or none if the id does not exist
        """
        pass

    def get_sale_frequencies(self):
        """
        returns a dictionary where the keys are the sale amounts and the
        values are frequency of that sale amount
        """
        pass
