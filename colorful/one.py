import turtle 

NUMBER_OF_SHAPES = 100
SPEED = 0
SIDES = 4

loadWindow = turtle.Screen()
turtle.speed(SPEED)

for j in range(4):
	if j ==1:
		turtle.color('pink')
	if j ==2:
		turtle.color('red')
	if j ==3:
		turtle.color('blue')
	if j ==4:
		turtle.color('green')
	if j ==0:
		turtle.color('gold')
	if j ==5:
		turtle.color('black')
	if j ==6:
		turtle.color('silver')
	for i in range(NUMBER_OF_SHAPES+1):
		turtle.forward(i)
		turtle.left(360/SIDES)

turtle.exitonclick()