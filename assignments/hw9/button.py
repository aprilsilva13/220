from graphics import *


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.label = label
        self.text = Text(self.shape.getCenter(), label)

    def get_label(self):
        return self.label

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        if (point.getX() > self.shape.getP1().getX() and point.getX() < self.shape.getP2().getX()) and (point.getY() > self.shape.getP1().getY()) and (point.getY() < self.shape.getP2().getY()):
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.label.setText(self.label)