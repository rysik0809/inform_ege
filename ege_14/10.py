f = 5 * 216**1225 + 4 * 36**1256 - 4 * 6**1257 - 2023
count = 0
while f:
    if f % 6 == 5:
        count += 1
    f = f // 6
print(count)