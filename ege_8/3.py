from itertools import product
words = product('пир', repeat=5)
k = 0
for w in words:
    word = ''.join(w)
    if word.count('п') == 1:
        k += 1
print(k)
# Ответ: 80