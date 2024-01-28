from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("purple")
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.left(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.goto(0, -280)

