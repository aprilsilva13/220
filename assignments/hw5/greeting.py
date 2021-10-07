"""
April Silva
greeting.py
Description: Creating a greeting card
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""

from graphics import Circle, Point, Polygon, Line, GraphWin, Text
from time import sleep
import math


def heart(win):
    first_text = Text(Point(300, 30), "Happy Valentine's Day!")
    arc1 = Circle(Point(250, 250), 50)
    arc2 = Circle(Point(350, 250), 50)
    circle = Circle(Point(300, 275), 30)
    triangle = Polygon(Point(250-((50*math.sqrt(2))/2), 250+((50*math.sqrt(2)/2))), Point(300, 400), Point((350+((50*math.sqrt(2))/2)), 250+((50*math.sqrt(2))/2)))


    arc1.draw(win)
    arc2.draw(win)
    triangle.draw(win)
    circle.draw(win)
    first_text.draw(win)


    arc1.setFill("pink")
    arc2.setFill("pink")
    arc1.setOutline("pink")
    arc2.setOutline("pink")
    triangle.setFill("pink")
    triangle.setOutline("pink")
    circle.setFill("pink")
    circle.setOutline("pink")



def arrow(win):
    rectangle1 = Polygon(Point(68, 528), Point(71, 531),  Point(43, 568), Point(40, 565))
    triangle1 = Polygon(Point(75, 525), Point(65, 525), Point(75, 535))

    rectangle1.draw(win)
    rectangle1.setFill("red")
    rectangle1.setOutline("pink")
    triangle1.draw(win)
    triangle1.setFill("red")
    triangle1.setOutline("pink")


    for i in range(100):
        rectangle1.move(3,-3)
        triangle1.move(3,-3)
        sleep(0.1)
    closing_text = Text(Point(300,550), "Click anywhere to close")
    closing_text.draw(win)


def main():
    win = GraphWin("Happy Valentine's Day!", 600, 600)
    heart(win)
    arrow(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
