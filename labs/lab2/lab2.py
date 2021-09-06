"""
Name: April Silva
lab2.py
"""

def sum_of_threes():
    x = eval(input("Enter an upper bound: "))
    acc = 0
    for i in range(0, x + 1, 3):
        acc = acc + i
    print(acc)


def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(h * l, end=" ")
        print()

def triangle_area():
    import math
    a = eval(input("input a: "))
    b = eval(input("input b: "))
    c = eval(input("input c: "))
    s = a + b + c / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(area)

def sumSquares():
    start = eval(input("Enter a starting number: "))
    end = eval(input("Enter an ending number: "))
    acc = 0
    for i in range(start, end +1):
        acc += i **2
    print(acc)

def power():
    base = eval(input("Enter a base: "))
    exponent = eval(input("Enter an exponent: "))
    acc = 1
    for i in range(exponent):
        acc *= base
    print(acc)



