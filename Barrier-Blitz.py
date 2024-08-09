import turtle
from random import randint
from typing import Counter

# initialize screen game
wind = turtle.Screen()
wind.title('Barrier Blitz')
wind.bgcolor('yellow')
wind.setup(width=800, height=600)
wind.tracer(0) # stop auto update 

# barrier one 
barrier_one = turtle.Turtle()
barrier_one.speed(0)
barrier_one.shape('square')
barrier_one.color('red')
barrier_one.penup()
barrier_one.goto(-370, 0)
barrier_one.shapesize(stretch_wid=6,stretch_len=1)

# barrier two
barrier_two = turtle.Turtle()
barrier_two.speed(0)
barrier_two.shape('square')
barrier_two.color('blue')
barrier_two.penup()
barrier_two.goto(370, 0)
barrier_two.shapesize(stretch_wid=6 ,stretch_len=1)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('black')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2 # ball speed on x axis
ball.dy = 0.2 # ball speed on y axis

# score object
score1 = 0 
score2 = 0 
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle() 
score.goto(0,260)
score.write(" {} - {}".format(score1,score2), align="center", font=("Courier",24,"normal"))


# move barrier one up
def barrier_one_up():
    y = barrier_one.ycor()
    y += 60 # speed barrier up
    barrier_one.sety(y)

# move barrier two up
def barrier_two_up():
    y = barrier_two.ycor()
    y += 60 # speed barrier up
    barrier_two.sety(y)

# move barrier one down
def barrier_one_down():
    y = barrier_one.ycor()
    y -= 60 # speed barrier down
    barrier_one.sety(y)

# move barrier two down
def barrier_two_down():
    y = barrier_two.ycor()
    y -= 60  # speed barrier down
    barrier_two.sety(y)
    
    
# keyboard press
def move_barreir():
    wind.listen()
    wind.onkeypress(barrier_one_up, 'z')
    wind.onkeypress(barrier_one_down, 's')
    wind.onkeypress(barrier_two_up, 'Up')
    wind.onkeypress(barrier_two_down, 'Down')


# ball collision with barrier
def collision():
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < barrier_two.ycor() + 50 and ball.ycor() > barrier_two.ycor() -50 ):
        ball.setx(360)
        ball.dx *= -1

    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < barrier_one.ycor() + 50 and ball.ycor() > barrier_one.ycor() -50 ):
        ball.setx(-360)
        ball.dx *= -1
        


# boreder check
def check_border():
    global score1, score2  # Declare these variables as global to modify them
    
    #chack ball border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1        
    
    if ball.xcor() > 395:
        ball.dx *=-1
        ball.goto(0,0)
        score1 += 1
        score.clear() 
        score.write(" {} - {}".format(score1,score2), align="center", font=("Courier",24,"normal"))
    elif ball.xcor() < -395:
        ball.dx *= -1
        ball.goto(0,0)
        score2 += 1
        score.clear()
        score.write(" {} - {}".format(score1,score2), align="center", font=("Courier",24,"normal"))

    #check barrier border
    if barrier_one.ycor()>250:
        barrier_one.sety(250)
    elif barrier_one.ycor()<-250:
        barrier_one.sety(-250)
    
    if barrier_two.ycor()>250:
        barrier_two.sety(250)
    if barrier_two.ycor()<-250:
        barrier_two.sety(-250)


# ball movement
def move_ball():
    # move the ball
    ball.setx(ball.dx + ball.xcor())
    ball.sety(ball.dy + ball.ycor())

    check_border()

    collision()


# main function to program 
def main():
    while True:
        wind.update()
        move_barreir()
        move_ball()
          
main()