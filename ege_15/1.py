for a in range(1, 1000):
    fl = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((x - 30) < a) and ((15 - y) < a) or (x * (y + 3) > 60)) == False:
                fl = False
                break
        if fl == False:
            break
    if fl == True:
        print(a)
        break