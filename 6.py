# _________________________№1____________________
# n = {}
# k = 0
# for i in range(27):
#     k += 5
#     n[k] = not n.get(k, 0)
#     k -= 3
#     n[k] = not n.get(k, 0)
#     k -= 3
# print(sum(n.values()))

# _________________________№2_______________________
# from turtle import *
# left(90)
# tracer(0)
# screensize(2000, 2000)
# k = 20
# for i in range(2):
#     forward(13*k)
#     right(90)
#     forward(18*k)
#     right(90)
# pu()
# forward(5*k)
# right(90)
# forward(9*k)
# left(90)
# pd()
# for i in range(2):
#     forward(11*k)
#     right(90)
#     forward(7*k)
#     right(90)
# pu()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*k, y*k)
#         dot(5)
# done()
# # пересечение - часть которая перечекает 2 фигуры
# # объединение - все точки внутри 2 фегуры