import turtle 

NUMBER_OF_CIRCLES = 100
SPEED = 0
SIDES = 7

loadWindow = turtle.Screen()
turtle.speed(SPEED)

for x in range(3, SIDES):
	for i in range(NUMBER_OF_CIRCLES):
		turtle.forward(i)
		turtle.left(360/x)


turtle.exitonclick()