from turtle import *


t=Turtle()
t.screen.bgcolor("black")
colors=["blue","purple","red","yellow"]
 
for x in range(300):
    t.color(colors[x%4])
    t.fd(x)
    t.left(90)
 
t.screen.exitonclick()
t.screen.mainloop()