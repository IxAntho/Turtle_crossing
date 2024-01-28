import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
count = 6
cars = []
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    #  creating a new car every 6th time the loop runs
    if count % 6 == 0:
        car = CarManager()
        cars.append(car)

    #  moving every car and detecting collisions
    for car in cars:
        car.move(scoreboard.level)
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    #  Detecting when turtle has won a level
    if turtle.ycor() > 280:
        turtle.restart()
        scoreboard.update_scoreboard()
        for car in cars:
            car.restart()

    screen.update()
    count += 1

screen.exitonclick()
