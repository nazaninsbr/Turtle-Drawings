import turtle 

NUMBER_OF_CIRCLES = 200
SPEED = 0
SIDES = 4

loadWindow = turtle.Screen()
turtle.speed(SPEED)

for i in range(NUMBER_OF_CIRCLES):
	turtle.forward(i)
	turtle.left(360/SIDES)


turtle.exitonclick()