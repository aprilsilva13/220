"""
April Silva
interest.py

Description: Calculating interest for HW 2
I certify that this assignment is completely my own work.
"""

def main():
    print("This program calculates and outputs the monthly interest charge")
    rate = eval(input("Enter the annual interest rate: "))
    days = eval(input("Enter the number of days in the billing cycle: "))
    net = eval(input("Enter the previous net balance: "))
    payment = eval(input("Enter the payment amount: "))
    day = eval(input("Enter the day of the billing cycle when the payment was made: "))
    cycle = eval(input("Enter the billing cycle for the month: "))
    step1 = net * cycle
    step2 = rate * 11
    step3 = step1 - step2
    step4 = step3 / cycle
    print(step4)


if __name__ == '__main__':
    main()


