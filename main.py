from turtle import Screen 
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
initial_time = 0.1


screen = Screen()
screen.listen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()

ball = Ball()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True

while game_on:
        time.sleep(ball.initial_speed)
        screen.update()
        ball.ball_move()

        #detect collision
        if ball.ycor() > 280 or ball.ycor() < -280:
                ball.bounce()

        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
                ball.bounce_x()
                
                
                

        if ball.xcor() > 380:
                ball.reset()
                scoreboard.l_point()
        if ball.xcor() < -380:
                ball.reset()
                scoreboard.r_point()

        #if scoreboard.l_point() == 3 or scoreboard.r_point() == 3:
              #  game_on = False
              #  print("Game Over")
                
        

screen.exitonclick()
