H, W = map(int, input().split())
A = [input().split() for i in range(H)]
ans = 'Yes'

for i1 in range(H):
    for i2 in range(H):
        for j1 in range(W):
            for j2 in range(W):
                if i1 < i2 and j1 < j2:
                    if int(A[i1][j1]) + int(A[i2][j2]) > int(A[i2][j1]) + int(A[i1][j2]):
                        ans = 'No'

print(ans)
