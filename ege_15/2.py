def f(x, a):
    return ((x % a != 0) and (x % 21 == 0)) <= (x % 14 != 0)

for a in range(1, 1000):
    fl = True
    for x in range(1, 1000):
        if not (f(x, a)):
            fl = False
            break
    if fl:
        print(a)