for n in range(1, 1001):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 1:
        n2 = n2 + '1'
    else:
        n2 = n2 + '0'

    if n2.count('1') % 2 == 1:
        n2 = n2 + '1'
    else:
        n2 = n2 + '0'

    r = int(n2, 2)
    if r > 43:
        print(r)
        break
