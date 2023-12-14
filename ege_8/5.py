from itertools import product
words = product('елмру', repeat=4)
k = 0
for w in words:
    word = ''.join(w)
    k += 1
    if word[0] == 'л':
        print(k)
        break

# Ответ: 126