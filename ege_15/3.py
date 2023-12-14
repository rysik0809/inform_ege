s = []
for a1 in range(1, 101):
    for a2 in range(1, 101):
        fl = True
        for x in range(1, 101):
            if not (((a1 <= x <= a2) <= (10 <= x <= 29)) or (13 <= x <= 18)):
                fl = False
                break

        if fl:
            s.append(a2 - a1)
print(max(s))