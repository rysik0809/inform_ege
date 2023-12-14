for x in '123456789ABCDE':
    m = int('97968' + x + '13', 15)
    n = int('7' + x + '233', 15)
    if (m + n) % 14 == 0:
        print((m + n) // 14)
