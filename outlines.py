from turtle import Turtle

class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.width(10)
        self.color('black')
        self.ht()
        self.create_road()
        
    def create_road(self):
        self.up()
        go_x = 300
        self.seth(180)
        positions = [-250, -125, 0, 125, 250]
        for i in range(5):
            self.goto(go_x, positions[i])
            if i % 2 :
                for j1 in range(0, 300, 30):
                    self.up()
                    self.fd(30)
                    self.down()
                    self.fd(30)
            else :
                for j2 in range(0,300,30):
                    self.down()
                    self.fd(60)
            self.up()