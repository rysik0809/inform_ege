# _______________________№1_____________________________
# def f(x, a):
#     return (x % a != 0) <= ((x % 28 == 0) <= (x % 49 != 0))
# for a in range(1, 1000):
#     if all(f(x, a) == 1 for x in range(1, 1000)):
#         print(a)

# _______________________№2_____________________________
# from itertools import *
# def f(x):
#     b = 24 <= x <= 90
#     c = 47 <= x <= 115
#     a = a1 <= x <= a2
#     return c <= (((not a) and (b)) <= (not c))
# x0 = [i/4 for i in range(23*4, 116*4)]
# m = []
# for a1, a2 in combinations(x0, 2):
#     if all(f(x) for x in x0):
#         m.append(a2-a1)
# print(min(m))
