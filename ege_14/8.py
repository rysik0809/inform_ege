f = 25**5 + 5**15 - 25
count = 0
while f:
    if f % 5 == 4:
        count += 1
    f = f // 5
print(count)