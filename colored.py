import turtle 

NUMBER_OF_CIRCLES = 100
SPEED = 0

loadWindow = turtle.Screen()
turtle.speed(SPEED)
turtle.colormode(255)

for i in range(NUMBER_OF_CIRCLES):
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.left(i)
	r = (9*i)%255
	g = (6*i)%255
	b = (3*i)%255
	turtle.color(r, g, b)


turtle.exitonclick()