print('w x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if((x and not(y)) or (y == z) or not(w)) == False:
                    print(w, x, y, z)