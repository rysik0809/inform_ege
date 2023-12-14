def f(n):
    if n <= 1:
       return 0
    else:
        if n % 2 != 0:
            return 2 * n + f(n - 1)
        else:
            return 2 * f(n - 1)
print(f(24))

