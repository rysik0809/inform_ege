from itertools import product
words = product('агдепр', repeat=3)
count = 0
for w in words:
    word = ''.join(w)
    count += 1
    if word[0] == 'е':
        print(count)
        break
