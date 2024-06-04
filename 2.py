# from itertools import *
# def f(x, y, z, w):
#     return (not(x <= z)) or (y == w) or y
#
# for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
#     t = [(1, 0, a1, a2), (a3, 1, 0, a4), (0, a5, a6, a7)]
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(p)

# _________________________________________________________________

# from itertools import *
# def f(x, y, z, w):
#     return ((x <= y) or (z == x)) and (w <= z)
#
# t = [(0, 0, 1, 1), (0, 0, 1, 0), (0, 1, 1, 1)]
# for p in permutations('xyzw'):
#     if [f(**dict(zip(p, r))) for r in t] == [1, 0, 0]:
#         print(p)
