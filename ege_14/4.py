f = 9**26 + 3**78 - 9
count = 0
while f:
    if f % 3 == 2:
        count += 1
    f = f // 3
print(count)