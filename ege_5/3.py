for n in range(1, 1000):
    n2 = bin(n)[2:]
    for i in range(2):
        if n2.count('1') % 2 == 0:
            n2 += '0'
        else:
            n2 += '1'
    r = int(n2, 2)
    if r > 396:
        print(r)
        break
# ответ: 402