import sys
def f(n):
    if n == 1:
        return 3
    else:
        return 2 * n + 5 + f(n - 1)
sys.setrecursionlimit(10**5)
print(f(3026) - f(3024))