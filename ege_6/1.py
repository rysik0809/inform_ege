from turtle import *
tracer(0)
left(90)
k = 20
for i in range(2):
    right(120)
    forward(9 * k)
right(300)
for i in range(2):
    right(120)
    forward(9 * k)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()

# Ответ: 68