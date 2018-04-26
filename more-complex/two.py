import turtle 
from random import randint 

NUMBER_OF_CIRCLES = 50
NUMBER_OF_GROUPS = 3
SPEED = 0

loadWindow = turtle.Screen()
turtle.speed(SPEED)
turtle.colormode(255)

for i in range(NUMBER_OF_GROUPS):
	r = randint(0,255) 
	g = randint(0,255) 
	b = randint(0,255)
	for i in range(NUMBER_OF_CIRCLES):
		turtle.circle(i)
		turtle.left(i)
		
		turtle.pencolor(r, g, b)


turtle.exitonclick()