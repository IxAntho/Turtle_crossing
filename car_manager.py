from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.get_color()
        self.penup()
        self.left(180)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.get_location()

    def get_color(self):
        indx = random.randint(0, 5)
        self.color(COLORS[indx])

    def get_location(self):
        y_location = random.randint(-240, 240)
        self.goto(320, y_location)

    def move(self, level):
        self.forward(STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT)
        print(STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT)

    def restart(self):
        self.hideturtle()
