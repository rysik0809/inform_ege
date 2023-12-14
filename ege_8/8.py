from itertools import product
words = product('012345678', repeat=7)
k = 0
for w in words:
    word = ''.join(w)
    if word.count('8') == 1 and word[0] not in '1357' and word[-1] not in '02468' and word[0] != '0':
        k += 1
print(k)

# Ответ: 376832