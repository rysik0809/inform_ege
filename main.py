# from itertools import *         задание 2 
# def f(x, y, z, w):
#     return (not(x <= z)) or (y == w) or y
#
# for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
#     t = [(1, 0, a1, a2), (a3, 1, 0, a4), (0, a5, a6, a7)]
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 print(p)

# s = []                          задание 5
# for N in range(1, 1000):
#     n = bin(N)[2:]
#     if N % 2 == 0:
#         n = '10' + n
#     if N % 2 != 0:
#         n = '1' + n + '01'
#     r = int(n, 2)
#     if r > 516:
#         s.append(N)
# print(min(s))

# from turtle import *           задание 6
# left(90)
# screensize(2000, 2000)
# k = 15
# tracer(0)
# for i in range(2):
#     forward(21*k)
#     right(90)
#     forward(27*k)
#     right(90)
# pu()
# forward(9*k)
# right(90)
# forward(10*k)
# left(90)
# pd()
# for i in range(2):
#     forward(86*k)
#     right(90)
#     forward(47*k)
#     right(90)
# pu()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*k, y*k)
#         dot(5)
# done()

# from itertools import *                задание 8
# words = product('апрсу', repeat=5)
# k = 0
# for w in words:
#     word = ''.join(w)
#     k += 1
#     if word.count('у') <= 1 and 'аа' not in word:
#         print(k, word)

# c = 0                                  задание 9
# for line in open('t.txt'):
#     a = [int(x) for x in line.split()]
#     if max(a) < (sum(a) - max(a)):
#         if (a[0]+a[1] == a[2]+a[3]) or (a[0]+a[2] == a[1]+a[3]) or \
#                 (a[0] + a[3] == a[2] + a[1]):
#             c += 1
# print(c)

# s = '8' * 82                          задание 12
# while ('1111' in s) or ('8888' in s):
#     if '1111' in s:
#         s = s.replace('1111', '8', 1)
#     else:
#         s = s.replace('8888', '11', 1)
#
# print(s)

# s = 2 * 729**2014 + 2 * 243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2 * 9**2022 - 2024   задание 14
# k = 0
# while s > 0:
#     if s % 27 > 9:
#         k += 1
#     s = s // 27
# print(k)

# for a in range(1, 1000):                            задание 15
#     f = True
#     for x in range(1, 1000):
#         if not ((x % a != 0) <= ((x % 14 == 0) <= (x % 4 != 0))):
#             f = False
#     if f:
#         print(a)

# from functools import *                              задание 16
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * f(n-1)
# for i in range(2024):
#     f(i)
# print((f(2024) - f(2023))/f(2022))

# a = [int(x) for x in open('t.txt')]                  задание 17
# m = min(x for x in a if x % 19 == 0)
# k = []
# for i in range(len(a) - 1):
#     if (a[i] % m == 0) or (a[i+1] % m == 0):
#         k.append(a[i] + a[i+1])
# print(len(k), max(k))

# def f(a, b, m):                                      задание 19 - 21
#     if (a + b) >= 59: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(a+1, b, m-1), f(a*2, b, m-1), f(a, b+1, m-1), f(a, b*2, m-1)]
#     return any(h) if (m-1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 54) if f(5, s, 2)]) # all > any
# print('20)', [s for s in range(1, 54) if not f(5, s, 1) and f(5, s, 3)])
# print('21)', [s for s in range(1, 54) if f(5, s, 4) and not f(5, s, 2)])

# def f(c, e):                                        задание 23
#     if c == e: return 1
#     if c > e: return 0
#     if c < e: return f(c+1 , e) + f(c+2, e) + f(c*2, e)
#
# print(f(4, 11)*f(11, 13)*f(13, 15))

# from fnmatch import *                                задание 25
# for x in range(0, 10**10, 1917):
#     if fnmatch(str(x), '3?12?14*5'):
#         print(x, x // 1917)

# print((317 * 13 * 262144)/(2**23))

# print((1024*960*13*160) / 14680064)

# from ipaddress import *                              задание 13
# k = 0
# net = ip_network('122.159.136.144/255.255.255.248', 0)
# for ip in net:
#     if (bin(int(ip))[2:]).count('1') % 4 != 0:
#         k += 1
# print(k)
