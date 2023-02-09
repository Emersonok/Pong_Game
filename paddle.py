from turtle import Turtle
paddles = []
starting_position = [(0,0), (0, 10), (0,20), (0,30), (0,40), (0,50)]
new_position = [(350,0), (350, 10), (350,20), (350,30), (350,40), (350,50)]


class Paddle:
    for blocks in range (6):
        paddle = Turtle("square")
        paddle.penup()
        paddle.color("white")
        paddle.goto(starting_position[blocks])
        paddle.goto(new_position[blocks])
        paddles.append(paddle)

    def up_movement():
        paddles.setheading(90)
        paddles.forward(20)
    def down_movement():
        paddles.setheading(270)
        paddles.forward(20)