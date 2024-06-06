# _______________________№1_____________________________
# def f(s,m):
#     if s >= 435: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s+5, m-1), f(s*3, m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)   |если 1-й ход может быть неудачным
# print('19)', [s for s in range(1, 200) if not f(s, 1) and f(s, 2)])
# print('20)', [s for s in range(1, 200) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 200) if not f(s, 2) and f(s, 4)])

# _______________________№2_____________________________
# def f(a, b, m):
#     if a + b >= 59: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(a+1, b, m-1), f(a*2, b, m-1), f(a, b+1, m-1), f(a, b*2, m-1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
# # print('19', [s for s in range(1, 54) if f(5, s, 2)]) |any()
# print('20', [s for s in range(1, 54) if not f(5, s, 1) and f(5, s, 3)])
# print('21', [s for s in range(1, 54) if not f(5, s, 2) and f(5, s, 4)])

# _______________________№3_____________________________
# def f(a, b, m):
#     if a + b <= 36: return m%2 == 0
#     if m == 0: return 0
#     h = [f(a-3, b, m-1), f((a+1)//2, b, m-1), f(a, b-3, m-1), f(a, (b+1)//2, m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# print('19)', [s for s in range(17, 100) if f(20, s, 2)])
# print('20)', [s for s in range(17, 100) if not f(20, s, 1) and f(20, s, 3)])
# print('20)', [s for s in range(17, 100) if not f(20, s, 2) and f(20, s, 4)])
