from turtle import Screen
from player import Player
from car import Car
from score import Score
from outlines import Road
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Car()
score = Score()
road = Road()


screen.listen()
screen.onkeypress(player.move, 'Up')

state_of_game = True
while state_of_game:
	time.sleep(0.05)
	screen.update()
	car.create_car()
	car.move()
	for item in car.traffic:
		if item.distance(player) < 20:
			score.game_over()
			state_of_game = False
	if player.ycor() > 300:
		score.level_up()
		player.start_pos()
		car.level_up()

screen.exitonclick()
