from itertools import product
words = product('аекмнь', repeat=6)
k = 0
for w in words:
    word = ''.join(w)
    k += 1
    if word[0] != 'ь' and word.count('м') == 2 and word.count('а') <= 1:
        print(k)

# Ответ: 38866