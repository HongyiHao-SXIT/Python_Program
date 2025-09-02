#Drew a heart
import turtle

screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.color('red')
pen.fillcolor('red')
pen.speed(2)
pen.pensize(2)

pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.setheading(60)
pen.circle(-90, 200)
pen.forward(180)

pen.end_fill()

pen.hideturtle()

turtle.done()