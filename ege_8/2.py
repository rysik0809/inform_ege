from itertools import product
words = product('вишня', repeat=6)
k = 0
for w in words:
    word = ''.join(w)
    if word.count('в') <= 1 and word[0] != 'ш' and word[-1] != 'и' and word[-1] != 'я':
        k += 1
print(k)

# Ответ: 4352