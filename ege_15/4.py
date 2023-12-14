for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if not ((x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0))):
            fl = False
            break
    if fl:
        print(a)