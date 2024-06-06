# _______________________№1_____________________________
# s = open('24_15339.txt').readline()
# s = s.replace('B', 'A').replace('C', 'A').replace('7', '6').replace('8', '6').replace('9', '6')
# while 'AA' in s: s = s.replace('AA', 'A A')
# while '66' in s: s = s.replace('66', '6 6')
# print(max(len(c) for c in s.split()))

# _______________________№2_____________________________
# s = open('24.14_14647.txt').readline()
# s = s.split('A')
# m = 0
# for i in range(len(s) - 3):
#     c = s[i] + 'A' + s[i+1] + 'A' + s[i+2] + 'A' + s[i+3]
#     m = max(m, len(c))
# print(m)

# _______________________№3_____________________________
# s = open('24.14_14647.txt').readline()
# ind_XY = []
# for i in range(len(s)):
#     if s[i] == 'X' or s[i] =='Y':
#         ind_XY.append(i)
# m = 0
# for i in range(len(ind_XY) - 3):
#     start = ind_XY[i] + 1
#     end = ind_XY[i + 3] - 1
#     if s[ind_XY[i + 1]] != s[ind_XY[i + 2]]:
#         m = max(m, end - start + 1)
# print(m)