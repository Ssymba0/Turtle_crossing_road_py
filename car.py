from turtle import Turtle
import random

COLORS = ['red', 'blue', 'green', 'purple', 'magenta', 'yellow', 'orange', 'brown', 'cyan', 'dark magenta',
          'tomato', 'royal blue', 'deep sky blue', 'gold']
# x = random.randint(-300, 260)
# y = random.randint(-300, 260)


class Car():
    def __init__(self):
        super().__init__()
        self.left_traffic = []
        self.right_traffic = []
        self.carspeed = 5

    def create_left_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            vehicule = Turtle('square')
            vehicule.color(random.choice(COLORS))
            vehicule.shapesize(stretch_wid=1, stretch_len=2)
            vehicule.up()
            vehicule.goto(-300, random.randint(-230, -30))
            self.left_traffic.append(vehicule)

    def create_right_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            vehicule = Turtle('square')
            vehicule.color(random.choice(COLORS))
            vehicule.shapesize(stretch_wid=1, stretch_len=2)
            vehicule.up()
            vehicule.seth(180)
            vehicule.goto(300, random.randint(30, 230))
            self.right_traffic.append(vehicule)

#move left traffic
    def move_left(self):
        for car in self.left_traffic:
            car.fd(self.carspeed)

#move right traffic
    def move_right(self):
        for car in self.right_traffic:
            car.fd(self.carspeed)

    def level_up(self):
        self.carspeed += 5
