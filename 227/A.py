N, K , A = map(int, input().split())

# if K+A > N:
#     ans = K+A - N - 1 
# else:
#     ans = K+A-1

# x = K+A-1
# ans = x % N
# if ans == 0:
#     ans = 1

# if N == 1:
#     ans = 1
# else:
#     if K+A-1 > N:
#         x = K % N
#         ans = x+A-1
#     else:
#         ans = K+A-1
    
#     if ans == 0:
#         ans = N


per = []
for i in range(N):
    per.append(i+1)

now = A-1
for i in range(K):
    if now == N:
        now = 0
    now += 1



print(now)





