def f(n):
    if n > 25:
        return n * n + 2 * n + 1
    else:
        if n % 2 == 0:
            return 2 * f(n + 1) + f(n + 3)
        else:
            return f(n + 2) + 3 * f(n + 5)

k = 0
for i in range(1, 1001):
    if '0' not in str(f(i)):
        k += 1

print(k)