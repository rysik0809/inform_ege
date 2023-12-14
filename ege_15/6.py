s = []
for a1 in range(1, 101):
    for a2 in range(1, 101):
        fl = True
        for x in range(1, 201):
            if not ((17 <= x <= 54) <= (((37 <= x <= 83) and not (a1 <= x <= a2)) <= (not (17 <= x <= 54)))):
                fl = False
                break
        if fl:
            s.append(a2 - a1)
print(min(s))