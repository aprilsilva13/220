"""
Name: <April Silva>
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

def shooting_percentage():
    totalshots = eval(input("Enter the total number of shots: "))
    shotsmade = eval(input("Enter the number of shots made: "))
    shootingpercentage = totalshots / shotsmade * 100
    print("Shooting Percentage =", shootingpercentage)

def coffee():
    order = eval(input("Enter your coffee order: "))
    cost = ((10.50 + 0.86) * order) + 1.50
    print("Total cost =", cost)

def kilometers_to_miles():
    km = eval(input("Enter the number of kilometers traveled: "))
    conversion = km / 1.61
    print("Miles traveled =", conversion)


