# _______________________№1_____________________________
# def f(c, e):
#     if c == e: return 1
#     if c > e: return 0
#     if c == 16: return 0
#     if c < e: return f(c+1, e)+f(c+2, e)+f(c*3, e)
# print(f(2, 9)*f(9, 18))

# _______________________№2_____________________________
# def f(c, e, k):
#     if c > e: return 0
#     if c == e: return k<=2
#     if c<e: return f(c+1, e, k)+f(c*2, e, k+1)+f(c*3, e, k+1)
# print(f(1, 100, 0))