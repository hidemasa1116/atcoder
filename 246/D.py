N = int(input())

def f(a, b):
    return a**3 + (a**2)*b + a*(b**2) + b**3

X = float('inf')
j = 10**6

for i in range(10**6+1):
    while f(i, j) >= N and j >= 0:
        X = min(X, f(i, j))
        j -= 1
    





# if B % 2 == 0:
#     b = int(B/2)
#     for i in range(b):
#         for j in reversed(range(b, B)):
#             x = i**3 + (i**2)*j + i*(j**2) + j**3
#             # print(x)
#             if x >= N and x < ans:
#                 ans = x

# else:
#     b = int(B//2)
#     for i in range(b):
#         for j in reversed(range(b+1, B)):
#             x = i**3 + (i**2)*j + i*(j**2) + j**3
#             # print(x)
#             if x >= N and x < ans:
#                 ans = x

# print(ans)








# N = int(input())

# i = 0
# flg = 0
# while flg == 0:

#     A = N ** (1/3)

#     if A.is_integer():
#         print(N)
#         exit(0)
        
#     B = int(A+1+i) 
#     ans = float('inf')

#     for i in range(B):
#         a = i
#         b = B - i
#         x = a**3 + (a**2)*b + a*(b**2) + b**3
#         if x < ans:
#             if x >= N:
#                 ans = x
#                 flg = 1
    
#     i += 1

# print(ans)

































# # if B % 2 == 0:
# #     a = B / 2
# #     b = B / 2
# # else:
# #     a = B // 2 + 1
# #     b = B // 2

# print('a:', a, 'b:', b)
# print((a+b)**3 - 2*a*b*(a+b))








