"""
Name: April Silva
lab9.py
"""
from graphics import *
import math

def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc

def toNumbers(strNums):
    for i in range(len(strNums)):
        strNums[i] = float(strNums[i])

def writeSumofSquares():
    infile = input("input numbers")
    outfile = input("enter output file")
    readfile = open(infile, "r")
    writefile = open(outfile, "w")
    for line in readfile:
        nums = line.split()
        toNumbers(nums)
        squareEach(nums)
        summation = sumList(nums)
        writefile.write("Sum of squares = " + str(summation))

def starter():
    weight = eval(input("Enter the weight: "))
    wins = eval(input("Enter the amount of wins: "))
    if 150 <= weight < 160 and wins >= 5 or weight > 199 or wins > 20:
        print("Is able to start")
    else:
        print("Is not able to start")


def leapYear(year):
    if year / 400 == 0 and (year / 100 != 0 or year / 400 == 0):
        return year

def circleOverlap():
    win = GraphWin("Circles", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, r)
    c1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p3.getX()) ** 2 + (p4.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, r2)
    c2.draw(win)

    distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + p1.getY() - p3.getY() ** 2 )

    if distance <= r + r2:
        text1 = Text("Circles overlap")
    else:
        text2  = Text("Circles don't overlap")


    win.getMouse()
    win.close()

def main():
    addTen(1, 2, 3)
    squareEach(1, 2, 3)
    sumList(1, 2, 3)
    toNumbers(1, 2, 3)
    writeSumofSquares()
    starter()
    leapYear(2000)
    circleOverlap()

main()
