# import required modules
import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("yellow")
wn.setup(width = 600, height = 600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("Black")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
food.color(random.choice(['green']))
food.shape(random.choice(['turtle']))
food.speed(0)
food.penup()
food.goto(0, 100)

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0", align="center", font=("Verdana", 24, "bold"))

# Functions to control the snake's direction
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Function to move the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Snake body segments
segments = []

# Main game loop
while True:
    wn.update()

    # Collision with screen borders
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
        score = 0
        delay = 0.1

    # Collision with food
    if head.distance(food) < 20:

        # Move the food to a random spot
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red") #tail color
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("Verdana", 24, "bold"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Checking for head collisions with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Verdana", 24, "bold"))

    time.sleep(delay)

wn.mainloop()

'''
Here's a line-by-line breakdown of the provided Python code for a Snake Game:

Import required modules:
The turtle module is used for creating graphics.
The time module introduces delays in execution.
The random module is used for generating random values (like food positions).

Set delay:
delay = 0.1: This controls the game speed.

Initialize scores:
score and high_score are used to track the player's progress.

Create a window screen:
A window (wn) is created with a title "Snake Game," a yellow background, and dimensions 600x600.
wn.tracer(0) turns off automatic updates for smoother animation.

Create the snake's head:
A turtle object (head) represents the snake's head.
Initial properties: square shape, black color, positioned at (0, 0), with no initial movement (direction = "Stop").

Create the food:
Another turtle object (food) represents food in the game.
Its color and shape are randomly selected.
Positioned initially at (0, 100).

Create the scoreboard:
A turtle object (pen) displays the score.
Positioned at the top of the screen with an initial message "Score: 0 High Score: 0".

Define direction control functions:
Functions go_up, go_down, go_left, and go_right change the head.direction, preventing 180-degree turns.

Define the snake's movement function:
Based on the head.direction, the move function updates the head's position:
"up": Move 20 units vertically.
"down": Move 20 units vertically in reverse.
"left": Move 20 units horizontally in reverse.
"right": Move 20 units horizontally.

Set keyboard controls:
Use wn.listen() to enable key listening.
Bind W, A, S, D keys to respective movement functions.

Initialize the snake's body:
An empty list segments stores the snake's body parts.

Main game loop:
Continuously updates the game state until the window is closed.

Handle screen boundary collisions:
If the snake's head moves out of the screen's bounds:
Pause briefly, reset the snake's head and body, reset the score, and restart the game.

Handle collisions with food:
If the head is within 20 units of the food:
Relocate the food randomly.
Add a new segment to the snake.
Decrease delay (to increase game speed).
Increase the score and update the scoreboard.

Update the snake's body movement:
Move all segments of the body in reverse order to follow the head's movement.

Check collisions with the snake's body:
If the head touches any segment:
Reset the game after a brief pause.

Control game speed:
time.sleep(delay) slows the game loop based on the current delay value.

Keep the window active:
wn.mainloop() ensures the program waits for user interaction and doesn't close immediately.
'''