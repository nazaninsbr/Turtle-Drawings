from turtle import *


t=Turtle()
t.screen.bgcolor("black")
colors=["pink","purple","green","yellow"]
 
for x in range(300):
    t.color(colors[x%4])
    t.circle(x,90)
 
t.screen.exitonclick()
t.screen.mainloop()