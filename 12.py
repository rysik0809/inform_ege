# _______________________№1_____________________________
# k = []
# for n in range(3, 1000):
#     s = '8' + '4' * n
#     while ('11' in s) or ('444' in s) or ('8888' in s):
#         if '11' in s:
#             s = s.replace('11', '4', 1)
#         if '444' in s:
#             s = s.replace('444', '88', 1)
#         if '8888' in s:
#             s = s.replace('8888', '1', 1)
#     k.append(sum(map(int,str(s))))            | сумма цифр числа
# print(max(k))

# _______________________№2_____________________________
# s = '8' * 45
# while '1111' in s or '8888' in s:
#     if '1111' in s:
#         s = s.replace('1111', '88', 1)
#     else:
#         s = s.replace('8888', '11', 1)
# print(s)