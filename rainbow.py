import turtle
import math

# Setup
t = turtle.Turtle()
s = turtle.Screen()
colors = ['red', 'deeppink', 'hotpink', 'magenta', 'violet', 'purple']
s.bgcolor('black')
t.speed('fastest')
t.hideturtle()

# Heart function (parametric)
def draw_heart(scale):
    for angle in range(0, 360):
        t.pencolor(colors[angle % len(colors)])
        t.width(2)
        t.goto(
            scale * 16 * math.sin(math.radians(angle))**3,
            scale * (13 * math.cos(math.radians(angle)) - 
                     5 * math.cos(math.radians(2 * angle)) - 
                     2 * math.cos(math.radians(3 * angle)) - 
                     math.cos(math.radians(4 * angle)))
        )

# Move turtle to center
t.penup()
t.goto(0, 0)
t.pendown()

# Animation loop
while True:
    t.penup()
    t.goto(0, 0)
    t.pendown()
    draw_heart(10)

    # Erase with black, thicker stroke
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.pencolor('black')
    t.width(6)
    draw_heart(10)
