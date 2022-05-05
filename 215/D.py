import math
N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = []

for i in range(1, M+1):
    flg = 0
    for a in A:
        if math.gcd(a, i) != 1:
            break
        flg += 1
    if flg == N:
        ans.append(i)

print(len(ans))
for i in ans:
    print(i) 


