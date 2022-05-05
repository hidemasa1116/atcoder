N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))


dict_T = {i+1:t for i, t in enumerate(T)}
dict_sort = sorted(dict_T.items(), key=lambda x:x[1])
print(dict_sort)


# Ts = [int(0) for i in range(N)]
# Ts[0] = T[0]

# for j in range(N):
    
#     for i in range(1, N):
#         Ts[i] = (Ts[i-1]+S[i-1])
#     for i in range(N):
#         if Ts[i] < T[i]:
#             T[i] = Ts[i]
#     if j < N-1:
#         Ts[j+1] = min(T[j+1], Ts[j+1])
#     print(j, '回目', T)


# for i in range(N):
#     print(T[i])


# print(T)
# print(Ts)

# for i in range(N):
#     if T[i] < Ts[i]:
#         print(T[i])
#     else:
#         print(Ts[i])
    




