"""
April Silva
sales_force.py
Description: Homework 10
I certify that this assignment is entirely my own work.
"""

class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, filename):
        with open(filename, "r") as infile:
            for line in infile:
                employee_id = line[0]
                name = line[1]
                sales = line[2:]
                sales.split()
                sales_people = employee_id + name
                for sale in sales:
                    add_sale = add_sale + sales_people
                self.sales_people.append()

    def quota_report(self, quota, sales):
        total = self.sales
        if sales == quota:
            return True
        else:
            return False

    def top_seller(self, sales_people, sales, quota):
        for sales in sales_people:
            if sales >= quota:
                print(sales_people + "had" + sales + "total sales ")
            if sales <= quota:
                print(sales_people + "had less than the quota number of sales. They had" + sales + "sales ")


    def individual_sales(self, sales_people, sales, employee_id):
        for sales_people in sales:
            return employee_id
        return None