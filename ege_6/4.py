from turtle import *
tracer(0)
left(90)
k = 20

right(45)
for i in range(7):
    forward(5 * k)
    right(45)
    forward(10 * k)
    right(135)
pu()

for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()
