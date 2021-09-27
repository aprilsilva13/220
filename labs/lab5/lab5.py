"""
Name: April Silva
lab5.py
"""
import math

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)

    length1 = math.sqrt(p2.getX ** 2 - p1.getY ** 2)  #distance from a to b
    length2 = math.sqrt(p3.getX ** 2 - p2.getY ** 2)
    length3 = math.sqrt(p3.getX ** 2 - p1.getY ** 2)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    perimeter = length1 + length2 + length3
    sides = length1 + length2 + length3 / 2
    area = math.sqrt(sides * (sides - length1) * (sides - length2) * (sides - length3))

    ptext = Text(Point, "The perimeter is: " + str(perimeter))
    ptext.draw(win)
    atext = Text(Point, "The area is: " + str(area))
    atext.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    red_box = Entry(Point(30, 30), 3)
    red_box.draw(win)
    green_box = Entry(Point(70, 70), 3)
    green_box.draw(win)
    blue_box = Entry(Point(90, 90), 3)
    blue_box.draw(win)

    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    win.getMouse()
    for i in range(5):
        red_text = red_box.getText()
        red_text = int(red_text)
        green_text = green_box.getText()
        green_text = int(green_text)
        blue_text = blue_box.getText()
        blue_text = int(blue_text)
        color = color_rgb(red_text, green_text, blue_text)
        shape.setFill(color)
        win.getMouse()


    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    values = eval(input("Input a string: "))
    print(values[0])
    print(values[-1])
    print(values[2:6])
    print(values[0: ])
    print(values * 10)
    for i in values:
       print(i)
    print(len[values])


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = "hithere"
    x = sum(values[5] + values[2.5])
    x = [1] * 5
    x = [2.5, "there", (5, 10)]
    x = [2.5, "there", 6]
    x = [2.5, 5, float(values[-1])]
    x = (values[5] + values[2.5] + values(float[-1])
    length = len(values)
    print(length)
    print(x)


def another_series():
    n = eval(input("Enter terms: "))
    acc = 0
    for i in range(n):
        y = 2 + (2 * (i%3))
        print(y, end=" ")
        acc = acc + y
    print(acc)





def main():
    # target()
    # triangle()
    color_shape()
   # pass


main()
