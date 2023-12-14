def f(n):
    if n <= 15:
        return 2 * n * n + 4 * n + 3
    else:
        if n % 3 == 0:
            return f(n - 1) + n * n + 3
        else:
            return f(n - 2) + n - 6
k = 0
for n in range(1, 1001):
    x = str(f(n))
    if len([i for i in x if int(i) % 2]) == len(x):
        k += 1
print(k)
