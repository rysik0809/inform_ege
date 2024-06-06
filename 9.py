# _______________________№1_____________________________
# k = 0
# for line in open('ggg.txt'):
#     a = [int(x) for x in line.split()]
#     a2 = [x for x in a if a.count(x) == 2]
#     a1 = [x for x in a if a.count(x) == 1]
#     if len(a2) == 2 and len(a1) == 5:
#         m = sorted(a1)
#         if m[0] * m[1] * m[2] > a2[0]**2:
#             k += 1
# print(k)

# _______________________№2_____________________________
# k = 0
# for line in open('ggg.txt'):
#     a = [int(x) for x in line.split()]
#     if max(a) < sum(a) - max(a):
#         if a[0] + a[1] == a[2] + a[3] or a[0] + a[2] == a[1] + a[3] or a[0] + a[3] == a[2] + a[1]:
#             k += 1
# print(k)