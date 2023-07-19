from turtle import Turtle

POSITIONS = [(0, 0), (20, 0), (40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for position in POSITIONS:
            self.add_snake(position)
    def add_snake(self,position):
        self.new_snake = Turtle("square")
        self.new_snake.color("white")
        self.new_snake.penup()
        self.new_snake.goto(position)
        self.snakes.append((self.new_snake))
    def extand(self):
        self.add_snake(self.snakes[-1].position())
    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            x_axis = self.snakes[i - 1].xcor()
            y_axis = self.snakes[i - 1].ycor()
            self.snakes[i].goto(x_axis, y_axis)
        self.snakes[0].fd(20)

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)
    def delet_snake(self):
        for seg in self.snakes:
            seg.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()