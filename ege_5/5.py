for n in range(1, 1001):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 = n2 + '0'
    else:
        n2 = n2 + '1'

    if n2.count('1') % 2 == 0:
        n2 = n2 + '0'
    else:
        n2 = n2 + '1'
    r = int(n2, 2)
    if r > 100:
        print(n)
        break