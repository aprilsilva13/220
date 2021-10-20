"""
Name: April Silva
vigenere.py
Description: Homework 6
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""
from graphics import *

def main():
    win = GraphWin("Vigenere", 400, 400)
    win.setCoords(0, 0, 10, 10)
    message_text = Text(Point(5, 10), "Message to code: ")
    keyword_text = Text(Point(5, 20), "Enter keyword: ")

    message_text.draw(win)
    keyword_text.draw(win)

    x = message_text
    y = keyword_text
    acc = ""
    for i in range(len(x)):
        c = ord(x[i])
        key = ord(y[i])
        result = c + key - 97
        acc += chr(result)
        print(acc)
    x.getText()
    y.getText()

def button(point1, point2, button_text, win):
    outline = Rectangle(point1, point2)
    center = outline.getCenter()
    label = Text(center, button_text)
    outline.draw(win)
    label.draw(win)

def draw_button():
    button("Encode", Point(2,2), Point(4,4))





    if __name__ == '__main__':
        main()