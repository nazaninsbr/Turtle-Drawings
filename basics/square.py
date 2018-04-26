from turtle import Turtle
t=Turtle()
t.shape("turtle")
t.screen.bgcolor('black')
t.color('pink')


for steps in range(4):
		t.fd(100)
		t.left(90)


t.screen.exitonclick()