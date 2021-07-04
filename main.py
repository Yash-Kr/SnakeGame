from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game - by YASH")
screen.tracer(0)

starting_pos = [(0, 0), (-20, 0), (-40, 0)]

segments = []

snake = Snake()
food = Food()

score_turtle = Score()
score_turtle.update_score()

screen.listen()

screen.onkey(snake.up, "Up")    #Note : Keys written are case sensitive
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    #detect collision with food
    if snake.head.distance(food) <= 15:      #distance method can take Turtle arguments  to compare dist of 2 turtles
        food.new_location()
        score_turtle.update_score()
        snake.extend()

    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_turtle.game_over()
        is_game_on = False

    #detect collision with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) <= 10:
            score_turtle.game_over()
            is_game_on = False
            break













screen.exitonclick()
