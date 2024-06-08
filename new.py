import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# Creating border
border = turtle.Turtle()
border.speed(5)
border.pensize(4)
border.penup()
border.goto(-310, 250)
border.pendown()
border.color("red")
border.forward(600)
border.right(90)
border.forward(500)
border.right(90)
border.forward(600)
border.right(90)
border.forward(500)
border.right(90)
border.penup()
border.hideturtle()

# Score variables
score = 0
high_score = 0
delay = 0.1

# Snake setup
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Food setup
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

# Snake body segments
old_fruit = []

# Scoring setup
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "bold"))

# Define movement functions
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

def reset_game():
    global score, delay, old_fruit
    time.sleep(1)
    snake.goto(0, 0)
    snake.direction = "stop"
    for segment in old_fruit:
        segment.goto(1000, 1000)  # Move segments off-screen
    old_fruit.clear()
    score = 0
    delay = 0.1
    update_score()

def update_score():
    scoring.clear()
    scoring.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "bold"))

def check_collision():
    global score, high_score, delay
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        score += 1
        if score > high_score:
            high_score = score
        update_score()
        delay -= 0.001

        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()
        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)

def game_over():
    global high_score
    time.sleep(1)
    screen.clear()
    screen.bgcolor('black')
    scoring.goto(0, 0)
    scoring.write("GAME OVER\nYour Score: {}\nHigh Score: {}\nClick anywhere to Restart".format(score, high_score), align="center", font=("Courier", 30, "bold"))
    screen.onclick(restart_game)

def restart_game(x, y):
    screen.onclick(None)  # Disable click handler while resetting the game
    screen.clear()
    screen.bgcolor("#1d1d1d")
    setup_border()
    reset_game()
    main_loop()

def setup_border():
    border.penup()
    border.goto(-310, 250)
    border.pendown()
    border.color("red")
    border.pensize(4)
    border.forward(600)
    border.right(90)
    border.forward(500)
    border.right(90)
    border.forward(600)
    border.right(90)
    border.forward(500)
    border.right(90)
    border.penup()
    border.hideturtle()

# Keyboard shortcuts
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

def main_loop():
    global delay
    while True:
        screen.update()
        check_collision()
        snake_move()

        if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
            game_over()
            break

        for food in old_fruit:
            if food.distance(snake) < 20:
                game_over()
                break

        time.sleep(delay)

setup_border()
reset_game()
main_loop()
turtle.done()
