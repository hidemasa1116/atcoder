N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

ans = 0

for i in range(N):
    for j in range(N):
        x1 = x[i]
        y1 = y[i]
        x2 = x[j]
        y2 = y[j]
        l =  ((x2-x1)**2 + (y2-y1)**2)**(1/2)
        if l > ans:
            ans = l

print(ans)


