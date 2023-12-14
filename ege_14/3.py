f = (2*343**123+2401)*(3*343**137-2401)
count = 0
while f:
    if f % 7 == 6:
        count += 1
    f = f // 7
print(count)

# Ответ: 407