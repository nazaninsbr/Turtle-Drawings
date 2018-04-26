import turtle 

NUMBER_OF_CIRCLES = 40
SPEED = 0

loadWindow = turtle.Screen()
turtle.speed(SPEED)

for i in range(NUMBER_OF_CIRCLES):
	turtle.circle(5*i)
	turtle.left(i)


turtle.exitonclick()