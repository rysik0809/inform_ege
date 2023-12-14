for a in range(1, 2000):
    fl = True
    for x in range(1, 2000):
        if not(x % a != 0) <= ((x % 36 == 0) <= (x % 54 != 0)):
            fl = False
            break
    if fl:
        print(a)