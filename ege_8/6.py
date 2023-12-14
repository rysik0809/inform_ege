from itertools import product
words = product('аиоуэ', repeat=4)
k = 0
for w in words:
    word = ''.join(w)
    k += 1
    if word == 'иэуэ':
        print(k)
        break

# Ответ: 245