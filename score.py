from ctypes import alignment
from turtle import Turtle

align='center'
font=('Calibri', 15, 'bold')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.goto(0,260)
        self.ht()
        self.level = 0
        self.write(f'LEVEL {self.level}',align=align,font=font)
    
    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f'LEVEL {self.level}', align=align, font=font)
    
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=align, font=('Calibri', 20, 'bold'))