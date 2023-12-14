s = []
for a1 in range(1, 101):
    for a2 in range(1, 101):
        fl = True
        for x in range(1, 101):
            if not ((not (46 <= x <= 74)) <= (((56 <= x <= 85) and (not (a1 <= x <= a2))) <= (46 <= x <= 74))):
                fl = False
                break
        if fl:
            s.append(a2 - a1)
print(min(s))