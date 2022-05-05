N = int(input())
S = input()
L, R = [], []

for i, c in enumerate(S):
    if c == 'L':
        R.append(i)
    else:
        L.append(i)

print(*(L+[N]+R[::-1]))








# import array
# N = int(input())
# S = input()
# A = array.array('i', [0])



# if S[0] == 'R':
#     A.insert(1, 1)
# else:
#     A.insert(0, 1)

# n = A.index(1)
# for i in range(1, N):

#     if S[i] == 'R':
#         A.insert(n+1, i+1)
#         n = n+1
#     else:
#         if n != 0:
#             A.insert(n, i+1)
#             n = n
#         else:
#             A.insert(0, i+1)
#             n = 0

# A = [str(i) for i in A]
# print(' '.join(A))




