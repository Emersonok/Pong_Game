from turtle import Turtle, Screen 

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")

paddles = []
starting_position = [(0,0), (0, 10), (0,20), (0,30), (0,40), (0,50)]
new_position = [(350,0), (350, 10), (350,20), (350,30), (350,40), (350,50)]

def up_movement():
        paddle.setheading(90)
        paddle.forward(20)
def down_movement():
        paddle.setheading(270)
        paddle.forward(20)

for blocks in range (6):
        paddle = Turtle("square")
        paddle.penup()
        paddle.color("white")
        paddle.goto(starting_position[blocks])
        paddle.goto(new_position[blocks])
        paddles.append(paddle)


screen.listen()
screen.onkey(up_movement, "Up")
screen.onkey(down_movement, "Down")



    
    


screen.exitonclick()
