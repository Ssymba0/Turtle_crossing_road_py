from ctypes import alignment
from turtle import Turtle
from os import path
import pickle

align = 'center'
font = ('Calibri', 15, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.goto(0, 260)
        self.ht()
        self.level = 0
        self.maxlevel = 0
        self.import_maxlevel()
        self.update_score()

    def import_maxlevel(self):
        if path.exists('.\Cross_road\save.txt'):
            if path.getsize('.\Cross_road\save.txt'):
                with open('.\Cross_road\save.txt', 'rb') as f:
                    self.maxlevel = pickle.load(f)
            else:
                self.maxlevel = 0
        else:
            with open('.\Cross_road\save.txt', 'wb+') as f:
                pickle.dump(self.maxlevel, f)

    def update_score(self):
        self.clear()
        self.write(f'LEVEL {self.level} MAX LEVEL {self.maxlevel}', align=align, font=font)

    def level_up(self):
        self.clear()
        self.level += 1
        self.max_level()
        self.update_score()

    def max_level(self):
        if self.level > self.maxlevel:
            self.maxlevel = self.level
        with open('.\Cross_road\save.txt', 'wb') as f:
            pickle.dump(self.maxlevel, f)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=align, font=('Calibri', 20, 'bold'))
