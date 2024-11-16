import turtle as t

playerAscore = 0
playerBscore = 0

# Create a window and declare a variable called window and call the screen()
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

# Creating the left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Creating the right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# Code for creating the ball
ball = t.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(10, 10)
ballxdirection = 0.2
ballydirection = 0.2

# Code for creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0                    Player B: 0", align="center", font=('Arial', 24, 'normal'))

# Code for moving the left paddle
def leftpaddleup():
    y = leftpaddle.ycor()
    if y < 250:  # Limit paddle movement within the screen
        leftpaddle.sety(y + 60)

def leftpaddledown():
    y = leftpaddle.ycor()
    if y > -250:  # Limit paddle movement within the screen
        leftpaddle.sety(y - 60)

# Code for moving the right paddle
def rightpaddleup():
    y = rightpaddle.ycor()
    if y < 250:  # Limit paddle movement within the screen
        rightpaddle.sety(y + 60)

def rightpaddledown():
    y = rightpaddle.ycor()
    if y > -250:  # Limit paddle movement within the screen
        rightpaddle.sety(y - 60)

# Assign keys to play
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

# Game loop
while playerAscore < 20 and playerBscore < 20:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # Border setup
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerAscore += 1
        pen.clear()
        pen.write(f"Player A: {playerAscore}                    Player B: {playerBscore}", align="center", font=('Arial', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerBscore += 1
        pen.clear()
        pen.write(f"Player A: {playerAscore}                    Player B: {playerBscore}", align="center", font=('Arial', 24, 'normal'))

    # Handling the collisions with paddles
    if (340 < ball.xcor() < 350) and (rightpaddle.ycor() - 50 < ball.ycor() < rightpaddle.ycor() + 50):
        ball.setx(340)
        ballxdirection *= -1

    if (-350 < ball.xcor() < -340) and (leftpaddle.ycor() - 50 < ball.ycor() < leftpaddle.ycor() + 50):
        ball.setx(-340)
        ballxdirection *= -1

# Display the winner
pen.goto(0, 0)
if playerAscore == 20:
    pen.write("Player A Wins!", align="center", font=('Arial', 36, 'bold'))
else:
    pen.write("Player B Wins!", align="center", font=('Arial', 36, 'bold'))

# Keep the window open
window.mainloop()

'''
Here is a plain-text line-by-line explanation of the code for the Pong game:

Import turtle as t:
Provides the graphical tools for creating the game elements.

Initialize scores for players A and B:
Both scores start at 0.

Create the game window (window):
Sets the title to "The Pong Game."
Background color is green.
Screen size is set to 800x600.
tracer(0) turns off automatic screen updates for smoother animation.

Create the left paddle (leftpaddle):
Shape is a stretched square to resemble a paddle.
Positioned on the left side at (-350, 0).

Create the right paddle (rightpaddle):
Similar to leftpaddle but positioned on the right side at (350, 0).

Create the ball (ball):
Shape is a red circle.
Starts at (10, 10).
Moves diagonally with small x and y directional increments (ballxdirection and ballydirection).

Create the pen for the scoreboard (pen):
Positioned at the top center of the screen (0, 260).
Displays the initial scores.

Define functions to move the paddles:
leftpaddleup and leftpaddledown move the left paddle vertically within screen boundaries.
rightpaddleup and rightpaddledown do the same for the right paddle.

Set up key bindings:
Keys w and s control the left paddle (up and down, respectively).
Arrow keys Up and Down control the right paddle.

Game loop:
Repeats until either player reaches a score of 20.

Move the ball:
Updates the ball's position by adding ballxdirection and ballydirection to its current coordinates.

Handle ball collisions with the screen boundaries:
Reverses the ball's vertical direction if it hits the top or bottom of the screen.

Handle ball going out of bounds:
If the ball crosses the right edge, Player A scores 1 point, and the ball resets to the center.
Similarly, if the ball crosses the left edge, Player B scores.
Updates the scoreboard each time.

Handle ball collisions with paddles:
If the ball hits the right paddle, it bounces back in the opposite direction.
Similarly, for the left paddle.

Display the winner:
When one player scores 20 points, the loop ends, and the winner is displayed at the center of the screen.

Keep the window open:
The game window remains open until manually closed.

This code creates a simple Pong game with functional paddles, a moving ball, and a scoring system.
'''