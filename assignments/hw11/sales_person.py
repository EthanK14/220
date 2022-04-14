"""
Name: Ethan Kidwell

Problem:

Certificate of Authenticity
I certify that the work is entirely my own.
"""

class SalesPerson:
    """
    Creates a employee with a name, id number, and a list of their sales
    """



    def __init__(self, employee_id, name):
        """
        Creates the employee and sales list default is an empty list
        """

        self.employee_id = employee_id
        self.employee_name = name
        self.sales = []

    def get_id(self):
        """
        Returns the id number
        """
        return self.employee_id

    def set_name(self, name):
        """
        Sets the name of the employee and changes it
        """
        self.employee_name = name

    def get_name(self):
        """
        Returns the name of the employee
        """
        return self.employee_name

    def enter_sale(self, sale):
        """
        Appends a sale value to the sales list
        """
        self.sales.append(sale)

    def total_sales(self):
        """
        Totals the number of sales from the list and returns them as a float value
        """
        sale_total = 0.0
        for sale in self.sales:
            sale_total = sale_total + sale
        return sale_total

    def get_sales(self):
        """
        returns the sales list
        """
        return self.sales

    def met_quota(self, quota):
        """
        Checks the employee and see's if their sales total meets the quota value entered
        """
        sale_total = self.total_sales()
        if sale_total >= quota:
            return True
        return False

    def compare_to(self, other):
        """
         returns -1 if other has more in total sales than self, 1 if self has more in
         total sales than other, and 0 if their total sales are the same
        """
        if other.total_sales() < self.total_sales():
            return 1
        elif other.total_sales() > self.total_sales():
            return -1
        elif other.total_sales() == self.total_sales():
            return 0

    def __str__(self):
        return '{}-{}:{}'.format(self.employee_id, self.employee_name, self.sales)