for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if not (((x % a != 0) and (x % 35 == 0)) <= ((x % 21 != 0) or (x % 35 != 0))):
            fl = False
            break
    if fl:
        print(a)