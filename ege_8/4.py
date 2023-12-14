from itertools import product
words = product('агдепр', repeat=3)
k = 0
for w in words:
    word = ''.join(w)
    k += 1
    if word[0] == 'р':
        print(k)
        break

# Ответ: 181