for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if not((x % 35 != 0) and (x % a == 0)) <= ((x % 21 == 0) or (x % a != 0)):
            fl = False

    if fl:
        print(a)