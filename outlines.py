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
        go_y = -255
        self.goto(go_x, go_y)
        self.seth(180)
        positions = [-100, 50, 150, 255]
        for i in range(1,5):
            if i % 2 :
                for j1 in range(0,300,30):
                    self.down()
                    self.fd(60)
            else :
                for j2 in range(0, 300, 30):
                    self.up()
                    self.fd(30)
                    self.down()
                    self.fd(30)
            self.up()
            self.goto(go_x, positions[i - 1])