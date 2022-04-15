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

    def __add_employee(self, employee_list):
        """
        edits a list of employees and takes each employee adds them to a list within the
        sales_people list. Then takes and splits their id #, name into their own elements
        and takes their sales and splits them into their own list within the employee's
        list. it then takes all this data and adds it all of it to create and return a list
        of employee objects.
        """

        # loops through list of sales people
        for num in range(len(employee_list)):  # loops through the first element of the list
            employee_list[num] = [employee_list[num]]  # adds that element to a list within the list
            # splits the name and id and sales into their own elements

            employee_list[num] = employee_list[num][0].split(', ')
            # splits all the sales into their own elements
            employee_list[num][2] = employee_list[num][2].split(' ')
            # creates them all as employee objects
            employee = SalesPerson(employee_list[num][0], employee_list[num][1])
            for sale in range(len(employee_list[num][2])):
                employee.enter_sale(employee_list[num][2][sale])  # adds sales to employee object
            self.sales_people.append(employee)


    def add_data(self, file_name):
        """
        Imports data from a file with the information of sales people and
        adds it all into a list
        """
        employee_file = open(file_name, 'r')
        employee_list = []
        for employee in employee_file.readlines():
            employee_list.append(employee[:-1])
        self.sales_people.append(self.__add_employee(employee_list))
        none_index = self.sales_people.index(None)
        self.sales_people.pop(none_index)

    def print_sales_force(self):
        for employee in self.sales_people:
            print(employee)

    def quota_report(self, quota):
        """
        Returns a list where each element is the sellers' employee id
        name, total sales, and a boolean value if the hit the quota value given
        """
        employee_list = []
        # loops through list of sales people

        # for num in range(len(self.sales_people) - 1):
        for employee in self.sales_people:  # loops through the first element of the list
            employee_total = employee.total_sales()

            if employee_total >= quota:
                employee_name = [employee.get_id(), employee.get_name(), employee.total_sales(), True]
                employee_list.append(employee_name)
            elif employee_total < quota:
                employee_not = [employee.get_id(), employee.get_name(), employee.total_sales(), False]
                employee_list.append(employee_not)

        return employee_list

    def top_seller(self):
        """
        returns a list of the top most seller and in the case of a tie it should
        return all those with that value
        """
        top_seller_sales = 0
        seller_list = [SalesPerson(123, 'JOHN DOE')]
        for employee in self.sales_people:
            employee_sales = employee.total_sales()
            if top_seller_sales < employee_sales:
                seller_list.pop(0)
                seller_list.insert(0 ,employee)

                top_seller_sales = employee.total_sales()
            elif top_seller_sales == employee_sales:

                seller_list.append(employee)

        return seller_list



    def individual_sales(self, employee_id):
        """
        Returns the sales person of the given id or None if the id does not exist
        """
        for employee in self.sales_people:
            if employee.get_id() == int(employee_id):
                return employee
        return None



    def get_sale_frequencies(self):
        """
        returns a dictionary where the keys are the sale amounts and the
        values are frequency of that sale amount
        """
        pass
