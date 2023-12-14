from itertools import product
words = product('пир', repeat=5)
count = 0
for w in words:
    word = ''.join(w)
    if word.count('п') == 1:
        count += 1
print(count)