N = int(input())
S = list(map(int, input().split()))

ans = N
for i in range(N):
    flg = 0
    for a in range(1, S[i]//3+2):
        for b in range(1, S[i]//3+2):
            if 4*a*b + 3*a + 3*b == S[i]:
                flg += 1
    if flg > 0:
        ans -= 1


print(ans)



