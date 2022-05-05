N = int(input())
ans = 0
for i in range(N):
    X = list(map(int, input().split()))
    ans += (X[1])*(X[1]+1)/2 - (X[0]-1)*X[0]/2

print(int(ans))








