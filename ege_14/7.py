f = 100**10 - 10**6 + 100
count = 0
while f:
    if f % 10 == 0:
        count += 1
    f = f // 10
print(count)