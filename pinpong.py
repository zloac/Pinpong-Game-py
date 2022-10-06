import turtle

pencere = turtle.Screen()
pencere.title("Miypop")
pencere.bgcolor("black")
pencere.setup(width=800, height=600)
pencere.tracer(0)

raket_a = turtle.Turtle()
raket_a.speed(0)
raket_a.shape('square')
raket_a.color('orange')
raket_a.penup()
raket_a.goto(-350, 0)
raket_a.shapesize(5, 1)

raket_b = turtle.Turtle()
raket_b.speed(0)
raket_b.shape('square')
raket_b.color('orange')
raket_b.penup()
raket_b.goto(350, 0)
raket_b.shapesize(5, 1)

ball = turtle.Turtle()
ball.speed(1)
ball.shape('circle')
ball.color('purple')
ball.penup()
ball.shapesize(1.5, 1.5)
ball.dx = 0.15
ball.dy = 0.15

def raket_a_up():
    y = raket_a.ycor()
    y = y + 20
    raket_a.sety(y)

def raket_a_down():
    y = raket_a.ycor()
    y = y - 20
    raket_a.sety(y)

def raket_b_up():
    y = raket_b.ycor()
    y = y + 20
    raket_b.sety(y)

def raket_b_down():
    y = raket_b.ycor()
    y = y - 20
    raket_b.sety(y)    


pencere.listen()
pencere.onkeypress(raket_a_up, 'w')
pencere.onkeypress(raket_a_down, 's')
pencere.onkeypress(raket_b_up, 'Up')
pencere.onkeypress(raket_b_down, 'Down')








while True:
    pencere.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.dy = ball.dy * -1

    if ball.xcor()>385 or ball.xcor()<-385:
        ball.dx = ball.dx * -1