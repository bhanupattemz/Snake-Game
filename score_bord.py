
from turtle import Turtle
FONT=("courier", 12, "normal")
ALIGN="center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt",mode="r") as file_read:
            self.higest_score=int(file_read.read())
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color("white")
        self.print_score()

    def score_maintain(self):
        self.score+=1
        self.print_score()

    def print_score(self):
        self.goto(0, 270)
        self.clear()
        self.write(f"score: {self.score}  Higest score: {self.higest_score}", move=True, align="center",
                   font=("Arial", 16, "normal"))
    def reset_score(self):
        self.goto(0,0)
        if self.score>self.higest_score:
            self.higest_score=self.score
            with open("data.txt", mode="w") as file_write:
                   file_write.write(str(self.higest_score))
        self.score=0
        self.print_score()


