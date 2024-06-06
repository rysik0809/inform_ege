# _______________________№1_____________________________
# from functools import *
# @lru_cache(None)
# def f(n):
#     if n <= 3:
#         return 2025
#     if n > 3:
#         return 3 * (n-1) * f(n-2)
# for i in range(1, 2027):
#     f(i)
# print(f(2027) / f(2023))

# _______________________№2_____________________________
# def f(n):
#     if n == 3:
#         return 1
#     if n > 3:
#         return 5 * f(n-1) + 6 * g(n-1) - 3*n + 8
# def g(n):
#     if n == 3:
#         return 1
#     if n > 3:
#         return 6 * f(n-1) + 5 * g(n-1) + 3
# print(f(9)+g(9))

# _______________________№3_____________________________
# from functools import *
# @lru_cache(None)
# def f(n):
#     if n < 3:
#         return n
#     if n > 2 and n % 2 != 0:
#         return f(n-1) + f(n-2) + 1
#     if n > 2 and n%2 == 0:
#         s = 0
#         for i in range(1, (n-1) + 1):
#             s += f(i)
#         return s
# print(f(38))