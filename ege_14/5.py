f = 9**18 + 3**54 - 9
count = 0
while f:
    if f % 3 == 2:
        count += 1
    f = f // 3
print(count)