import turtle
from playsound3 import playsound

# start the program
window = turtle.Screen()
window.title("Pong by Rayaan :)")

#background color
window.bgcolor("black")

# window height and width 
window.setup(width=800, height=600)
#stops window from updating
window.tracer(0)

# score for each player
score_a = 0
score_b = 0

# Paddle A
#-------------------------
paddle_a = turtle.Turtle()
#animation speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
# change shape size
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
# start at these cords
paddle_a.goto(-350, 0)



# Paddle B
paddle_b = turtle.Turtle()
#animation speed
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
# change shape size
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
# start at these cords
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
#animation speed
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
# start at these cords
ball.goto(0, 0)

# ball movement (change by x and y by 2 pixels)
ball.dx = 0.3
ball.dy = 0.3

# scoring system through draw
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
# dont want to see pen only text
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 | Player B: 0", align="center", font=("Courier", 24, "normal"))


# functions for paddle movement
def paddle_a_up():
    # get the cords and change them
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    # get the cords and change them
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    # get the cords and change them
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    # get the cords and change them
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    


#keyboard binding to function
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")



#Main game loop for each game
while True:
    # updates the screen every time the loop runs
    window.update()
    
    # set x and y coords to the new coords (move the ball)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # border checking to do when ball hits border
    # compare balls y coordinate (ball is 20x20)
    
    if ball.ycor() > 290:
        ball.sety(290)
        # basically reverses the direction
        ball.dy *= -1
        # asyncs the sound to the program, so runs in background
        playsound("Pong.wav", block=False)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        # basically reverses the direction
        ball.dy *= -1
        playsound("Pong.wav", block=False)
        
    # compare balls x coordinate (ball is 20x20) goes off the screen, so point to other
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        # update the score if out of bounds
        score_a += 1
        # clear the score before
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        # clear the score before
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            
    # paddle and ball collisions (paddle are 100px tall)
    # ball to the right , between top and bottom of paddle 
    if ball.xcor() > 340 and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        
    if ball.xcor() < -340 and (ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        
    # AI player (overwrites paddle b)
    # abs means absolute value, if its more than 20 it moves only, not always
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 20:
        paddle_b_up()
    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 20:
        paddle_b_down()
    
            
    