from turtle import *
tracer(0)
left(90)
k = 20

for i in range(2):
    forward(8 * k)
    right(90)
    forward(18 * k)
    right(90)
pu()
forward(4 * k)
right(90)
forward(10 * k)
left(90)
pd()
for i in range(2):
    forward(17 * k)
    right(90)
    forward(7 * k)
    right(90)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()