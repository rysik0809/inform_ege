from itertools import product
words = product('лмн', repeat=6)
k = 0
for w in words:
    word = ''.join(w)
    if word.count('л') == 1:
        k += 1

print(k)
# ответ: 192