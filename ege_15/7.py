s = []
for a1 in range(-10, 10):
    for a2 in range(-10, 10):
        fl = True
        for x in range(-10, 10):
            for y in range(-10, 10):
                if not (((a1 <= x <= a2) <= (x**2 <= 81)) and ((y**2 <= 36) <= (a1 <= y <= a2))):
                    fl = False
                    break
        if fl:
            s.append(a2 - a1)
print(max(s))