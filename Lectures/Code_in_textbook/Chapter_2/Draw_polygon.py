import turtle

sides = int(input("Please input the number of sides:"))

screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.color('red')
pen.fillcolor('red')
pen.speed(2)
pen.pensize(2)

angle = ((sides - 2) * 180) / sides

pen.begin_fill()
pen.left(angle)


pen.end_fill()

pen.hideturtle()

turtle.done()