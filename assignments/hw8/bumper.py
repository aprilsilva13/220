"""
April Silva
bumper.py
Description: Homework 8
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""

from random import randint
import math
from time import sleep
from graphics import GraphWin, Circle, Point, color_rgb

def main():
    win = GraphWin("Bumper", 500, 500)
    circle1 = Circle(Point(250, 250), 25)
    circle2 = Circle(Point(150, 350), 25)

    circle1.draw(win)
    circle2.draw(win)

    circle1.setFill(get_random_color())
    circle1.setOutline("purple")
    circle2.setFill(get_random_color())
    circle2.setOutline("light blue")

    circle1x = get_random(10)
    circle1y = get_random(10)
    circle2x = get_random(10)
    circle2y = get_random(10)

    while win.checkMouse() == None:
        sleep(.1)
        circle1.move(circle1x, circle1y)
        circle2.move(circle2x, circle2y)
        if did_collide(circle1, circle2):
            circle1x = circle1x * -1
            circle1y = circle1y * -1
            circle2x = circle2x * -1
            circle2y = circle2y * -1
        if hit_horizontal(circle1, win):
            circle1y = circle1y * -1

        if hit_horizontal(circle2, win):
            circle2y = circle2y * -1

        if hit_vertical(circle1, win):
            circle1x = circle1x * -1

        if hit_vertical(circle2, win):
            circle2x = circle2x * -1


def get_random(nums):
    x = randint(-nums, nums)
    return x


def did_collide(circle1, circle2):
    r = circle1.getRadius()
    r2 = circle2.getRadius()
    p1 = circle1.getCenter()
    p3 = circle2.getCenter()
    distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    if distance <= r + r2:
        return True
    else:
        return False

def hit_vertical(ball, win):
    centerpoint = ball.getCenter()
    cx = centerpoint.getX()
    radius = ball.getRadius()
    if cx + radius >= win.getWidth() or cx - radius <= 0:
        return True
    else:
        return False

def hit_horizontal(ball, win):
    centerpoint = ball.getCenter()
    cy = centerpoint.getY()
    radius = ball.getRadius()
    if cy + radius >= win.getHeight() or cy - radius <= 0:
        return True
    else:
        return False

def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return color_rgb(r, g, b)

if __name__ == "__main__":
    main()