N, X = map(int, input().split())
A = list(map(int,input().split()))

A_dict = {}
for i in range(N):
    A_dict[i+1] = 0
    

ans = 0

for i in range(N):
    if A_dict[X] == 0:
        ans += 1
        A_dict[X] = 1
        X = A[X-1]
    else:
        break

print(ans)




