# _______________________№1_____________________________
# a = [int(x) for x in open('ggg.txt')]
# m = max(x for x in a if x % 19 == 0)
# s = []
# for i in range(len(a) - 1):
#     if a[i] > m or a[i+1] > m:
#         s.append(a[i] + a[i+1])
# print(len(s), max(s))

# _______________________№2_____________________________
# a = [int(x) for x in open('ggg.txt')]
# m = max(x for x in a if abs(x) % 1000 == 121)
# s=[]
# for i in range(len(a)-2):
#     x, y, z = a[i], a[i+1], a[i+2]
#     if (((1000 <= abs(x) <= 9999) and abs(x) % 2 == 0) + \
#             ((1000 <= abs(y) <= 9999) and abs(y) % 2 == 0) + \
#             ((1000 <= abs(z) <= 9999) and abs(z) % 2 == 0)) <= 1:
#         if x + y + z <= m:
#             s.append(x+y+z)
# print(len(s), max(s))

# _______________________№3_____________________________
# if a[i]%8 == 7 and a[i]//8%8 != 2    |если пследняя цифра 7 а предпосл. не 2

# s = sum(int(x) for x in str(a[i]))