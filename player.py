from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.seth(90)
        self.start_pos()
        
    def move(self):
        self.fd(10)
    
    def start_pos(self):
        self.goto(0, -280)