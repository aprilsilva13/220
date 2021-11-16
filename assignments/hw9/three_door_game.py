from graphics import *
from button import Button
from random import *

def main():
    win = GraphWin("Three Door Game", 500, 500)
    button1 = Button(Rectangle(Point(62.5, 200), Point(125, 300)), "Door 1")
    button2 = Button(Rectangle(Point(187.5,200), Point(250, 300)), "Door 2")
    button3 = Button(Rectangle(Point(312.5, 200), Point(375, 300)), "Door 3")

    button1.draw(win)
    button2.draw(win)
    button3.draw(win)

    door_list = [button1, button2, button3]
    randNum = randint(0, 2)
    secret_door = door_list[randNum]
    instructions = Text(Point(250, 20), "Guess the secret door")
    instructions.draw(win)
    click = win.getMouse()
    if secret_door.is_clicked(click):
        secret_door.color_button("green")
        instructions.setText("You win!")
    else:
        if button1.is_clicked(click):
            button1.color_button("red")
        elif button2.is_clicked(click):
            button2.color_button("red")
        elif button3.is_clicked(click):
            button3.color_button("red")
        answer = Text(Point(250, 480), "Door " + str(randNum + 1) + " is my secret door!")
        answer.draw(win)
        instructions.setText("You lost!")
    win.getMouse()

main()
