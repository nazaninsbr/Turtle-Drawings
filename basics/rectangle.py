from turtle import Turtle
t=Turtle()
t.shape("turtle")
t.screen.bgcolor('black')
t.color('purple')


def slanted_rectangle(length,width,angle):
    t.setheading(angle)
    for steps in range(2):
        t.fd(width)
        t.left(90)
        t.fd(length)
        t.left(90)
 
slanted_rectangle(length=200,angle=45,width=100)
t.screen.exitonclick()