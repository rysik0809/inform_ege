from turtle import *
tracer(0)
left(90)
k = 20
for i in range(7):
    forward(12 * k)
    right(45)
    forward(6 * k)
    right(135)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()
# ответ: 44