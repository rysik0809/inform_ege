s = '1' + '9' * 100
while '19' in s or '299' in s or '3999' in s:
    if '19' in s:
        s = s.replace('19', '2', 1)

    if '299' in s:
        s = s.replace('299', '3', 1)

    if '3999' in s:
        s = s.replace('3999', '1', 1)

    print(s)