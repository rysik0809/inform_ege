# _______________________№1_____________________________
# from itertools import *
# words = product('0123456', repeat=7)
# k = 0
# for w in words:
#     word = ''.join(w)
#     if word[0] != '0':
#         word = word.replace('2', '0').replace('4', '0').replace('6', '0')
#         if word.count('0') == 2:
#             k += 1
# print(k)

# _______________________№2__________________________________

# from itertools import *
# words = product('апрсу', repeat=5)
# k = 0
# for w in words:
#     word = ''.join(w)
#     k += 1
#     if word.count('у') <= 1 and word not in 'аа':
#         print(k)

# _______________________№3__________________________________

# from itertools import product
# n = 0
# for word in product(sorted('ПРИВЫЧКА'), repeat = 5):
#     n += 1
#     if n % 5 != 0 and len(set(word)) == 5 and all(x not in word for x in 'ИЫА'):
#         print(n - n // 5)
#         break