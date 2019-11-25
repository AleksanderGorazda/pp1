import turtle

pen = turtle.Turtle()
def drawSquare(n,x,y):
    turtle.setheading(270)
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
