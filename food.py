from turtle import Turtle
from random import randint
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.refresh()

    def refresh(self):
        x_axis = randint(-280, 280)
        y_axis = randint(-280, 280)
        self.goto(x_axis, y_axis)