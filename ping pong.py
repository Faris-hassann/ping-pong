# import turtle module
import turtle

wind = turtle.Screen() # for screen
wind.title("ping pong") # title of the window
wind.bgcolor("black") # background color for the window
wind.setup(width=800, height=600) # width and height for the window
wind.tracer(0)

# first racket
firstRacket = turtle.Turtle()
firstRacket.speed(0)
firstRacket.shape("square")
firstRacket.shapesize(stretch_len=1, stretch_wid=5)
firstRacket.color("blue")
firstRacket.penup()
firstRacket.goto(-350, 0)


# second racket
secondRacket = turtle.Turtle()
secondRacket.speed(0)
secondRacket.shape("square")
secondRacket.shapesize(stretch_len=1, stretch_wid=5)
secondRacket.color("red")
secondRacket.penup()
secondRacket.goto(350, 0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player 1: 0  player 2: 0", align="center", font=("Arial",24,"normal"))


#won
won = turtle.Turtle()
won.speed(0)
won.color("white")
won.penup()
won.hideturtle()
won.goto(0, 0)


#functions
def firstRacket_up(): #function up for the blue team
    y = firstRacket.ycor()
    y += 20
    firstRacket.sety(y) 
 
def firstRacket_down(): #function down for the blue team
    y = firstRacket.ycor()
    y -= 20
    firstRacket.sety(y)


def secondRacket_up(): #function up for the red team
    y = secondRacket.ycor()
    y += 20
    secondRacket.sety(y) 

def secondRacket_down(): #function down for the red team
    y = secondRacket.ycor()
    y -= 20
    secondRacket.sety(y)

#keyboard bindings
wind.listen() 
wind.onkeypress(firstRacket_up, "w")
wind.onkeypress(firstRacket_down, "s")
wind.onkeypress(secondRacket_up, "Up")
wind.onkeypress(secondRacket_down, "Down")

# main loop for update
while True:
    wind.update()

    #movement of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1    

    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player 1: {}  player 2: {}".format(score1, score2), align="center", font=("Arial",24,"normal"))

    if ball.xcor() <-390:
        ball.goto(0, 0)
        ball.dx *= -1    
        score2 += 1
        score.clear()
        score.write("player 1: {}  player 2: {}".format(score1, score2), align="center", font=("Arial",24,"normal"))


    if score1 == 10:
        won.write("player 1 won", align = "center", font=("Arial", 30, "bold"))

    if score2 == 10:
        won.write("player 2 won" ,align="center", font=("Arial", 30, "bold"))

    #ball hits the rackets
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < secondRacket.ycor() + 40 and ball.ycor() > secondRacket.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < firstRacket.ycor() + 40 and ball.ycor() > firstRacket.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1