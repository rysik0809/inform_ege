f = 2 * 729**1021 - 2 * 243**1022 + 81**1023 - 2 * 27**1024 - 1025
count = 0
while f:
    if f % 3 == 0:
        count += 1
    f = f // 3
print(count)