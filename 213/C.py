H, W, N = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

As = sorted(set(A))
Bs = sorted(set(B))


Ad = {x: i+1 for i, x in enumerate(As)}
Bd = {x: i+1 for i, x in enumerate(Bs)}


for i in zip(A, B):
    print(Ad[i[0]], Bd[i[1]])
































# H, W, N = map(int, input().split())
# R = []
# C = []

# for _ in range(N):
#     r, c = map(int, input().split())
#     R.append(r)
#     C.append(c)
# print(R, C)

# Rs = sorted(set(R))  # `set`で重複を省いてソートしたリスト`Rs`
# Cs = sorted(set(C))
# print(Rs, Cs)

# # Rd = {Rs[i]: i+1 for i in range(len(Rs))} と同じです
# Rd = {x: i for i, x in enumerate(Rs, 1)}
# Cd = {x: i for i, x in enumerate(Cs, 1)}
# print(Rd, Cd)

# for r, c in zip(R, C):
#     print(Rd[r], Cd[c])





# H, W, N = map(int, input().split())
# X = [list(map(int, input().split())) for i in range(N)]

# for i in range(len(X)):
#     X[i].insert(0, i)

# n = []
# X_sort1 = sorted(X, key=lambda x:x[1])
# for i in range(len(X)):
#     n.append(X_sort1[i][1])
#     if i > 0:
#         if X[i][1] == n[i-1]:
#             X[i][1] = n[i-1]



# X_sort2 = sorted(X_sort1, key=lambda x:x[2])
# for i in range(len(X)):
#     X_sort2[i][2] = i+1


# X_sort3 = sorted(X_sort2, key=lambda x:x[0])
# for i in range(len(X)):
#     print(X_sort3[i][1], X_sort3[i][2])










