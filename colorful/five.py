from turtle import *
import random 

for n in range(15):
	penup()
	goto(random.randint(-200, 200), random.randint(-200, 200))
	pendown()

	redAmount = random.randint(0, 50)/100.0
	blueAmount = random.randint(50, 100)/100.0
	greenAmount = random.randint(0, 30)/100.0

	pencolor((redAmount, greenAmount, blueAmount))

	circleSize = random.randint(1, 40)
	pensize(random.randint(1, 5))

	for i in range(6):
		circle(circleSize)
		left(60)

exitonclick()