from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_running = True

while game_running:
    screen.update()
    time.sleep(0.01)
    ball.move()
    
    # Detect collision with the wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.x_move += 0.2
        ball.y_move += 0.2
        ball.bounce_x()
        print(ball.x_move)
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.x_move -= 0.2
        ball.y_move -= 0.2
        ball.bounce_x()
        print(ball.x_move)

    # Detect if the ball goes off the screen
    if ball.xcor() > 400:
        ball.reset_position()
        score.add_point("left")
    elif ball.xcor() < -400:
        ball.reset_position()
        score.add_point("right")


screen.exitonclick()
