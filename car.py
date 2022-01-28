from turtle import Turtle
import random

COLORS = ['red', 'blue', 'green', 'purple', 'magenta', 'yellow', 'orange', 'brown', 'cyan', 'dark magenta',
          'tomato', 'royal blue', 'deep sky blue', 'gold']
# x = random.randint(-300, 260)
# y = random.randint(-300, 260)


class Car():
    def __init__(self):
        super().__init__()
        self.traffic = []
        self.carspeed = 5

    def create_car(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            vehicule = Turtle('square')
            vehicule.color(random.choice(COLORS))
            vehicule.shapesize(stretch_wid=1, stretch_len=2)
            vehicule.up()
            vehicule.seth(180)
            vehicule.goto(300, random.randint(-250, 250))
            self.traffic.append(vehicule)

    def move(self):
        for car in self.traffic:
            car.fd(self.carspeed)

    def level_up(self):
        self.carspeed += 5