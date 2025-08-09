import turtle
import time

screen = turtle.Screen()
screen.bgcolor("darkblue")

writer = turtle.Turtle()
writer.color("silver")
writer.penup()
writer.goto(-200, 0)

text = "Helloo "

for x in range(-200, 201, 5):
    writer.clear()
    writer.goto(x, 0)
    writer.write(text, font=("Times New Roman", 100, "normal"))
    time.sleep(0.05)

screen.mainloop()
