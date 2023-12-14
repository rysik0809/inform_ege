# f = 4**12 + 2**32 - 16
# count = 0
# while f:
#     if f % 2 == 1:
#         count += 1
#     f = f // 2
# print(count)
print(bin(4**12 + 2**32 - 16).count('1'))