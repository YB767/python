import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
complete_count = 0
scoreboard = Scoreboard(complete_count)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars(complete_count)

    # Detect the collision turtle player with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Detect the player has reached the top edge of the screen
    player.check_complete(complete_count)


screen.exitonclick()
