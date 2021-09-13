"""
Name: April Silva
lab3.py
"""

def average():
    average = eval(input("Enter the number of grades: "))
    acc = 0
    for i in range(average):
       grades = eval(input("Enter you grade on Homework" + " " + str(i)))
    answer = acc + grades / average
    print("The average is", answer)

average()

def tip_jar():
    acc = 0
    for i in range(5):
        tip = eval(input("How much was the tip? "))
        acc = acc + tip
    print(tip)

tip_jar()


def newton():
    x = eval(input("Enter a value for x"))
    refine = eval(input("Enter the number of refines "))
    approx = x / 2
    for i in range(refine):
        approx = (approx + x / approx) / (2)
    print(approx)

newton()


def sequence():
    x = eval(input("Enter the number of terms in a series: "))
    for i in range(1, x+1):
        print(1 + i//2 * 2)

sequence()

def pi():
    ui = eval(input("Enter the number of terms in a series: "))
    acc = 1
    for i in range(ui):
        num = 2 + (i//2 * 2)
        den = 1 + ((i + 1) //2 * 2)
        acc = acc * (num / den)
    print(acc)

pi()
