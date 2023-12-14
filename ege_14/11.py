for x in '0123456789ABCDEF':
    n = int('135' + x + 'F', 16)
    m = int('9' + x + '531', 16)
    if (m + n) % 8 == 0:
        print((m + n) // 8)
        break