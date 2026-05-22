import turtle
import random

t = turtle.Turtle()
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
turtle.bgcolor("black")
t.speed(0)

for i in range(200):
    t.color(colors[i % 6])
    t.forward(i * 2)
    t.left(59)
    t.width(i // 100 + 1)
