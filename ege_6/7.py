from turtle import *
tracer(0)
left(90)
k = 20

right(90)
for i in range(3):
    right(45)
    forward(10 * k)
    right(45)
right(315)
forward(10 * k)
for i in range(2):
    right(90)
    forward(10 * k)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()