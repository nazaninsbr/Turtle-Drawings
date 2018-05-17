from turtle import Turtle

t=Turtle()


def backgroundColor():
	t.screen.bgcolor('yellow')

def drawFace():
	t.penup()
	t.goto(0, 100)
	t.color('#876B52')
	t.shape("circle")
	t.shapesize(5,4,1)
	t.fillcolor("#FCD5C4")


	t.color('#F3E2C6')
	for x in range(2):
		for i in range(100):
			t.fd(i)

if __name__ == '__main__':
	backgroundColor()
	drawFace()
	t.screen.exitonclick()