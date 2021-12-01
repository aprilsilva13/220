"""
April Silva
sales_person.py
Description: Homework 10
I certify that this assignment is entirely my own work.
"""

class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self,sale):
        self.sales.append(sale)

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        total = self.total_sales()
        if total > quota:
            return True
        else:
            return False

    def compare_to(self, other):
        mytotal = self.total_sales()
        othertotal = other.total_sales()
        if mytotal > othertotal:
            return 1
        elif othertotal > mytotal:
            return -1
        else:
            return 0

    def __str__(self):
        return str(self.employee_id) + "-" + self.name + ": " + str(self.total_sales())
