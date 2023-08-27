from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("violet")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_wall(self):
        #after bounce we only change y coordinates and x remains change for top and bottom walls, i.e., we reverse ball direction in y direction only
        self.y_move *= -1
    
    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_paddle()