for n in range(1, 1001):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = n2 + '00'
    else:
        n2 = n2 + '11'

    r = int(n2, 2)
    if r < 134:
        print(n)