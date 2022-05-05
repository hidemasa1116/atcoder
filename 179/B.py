N = int(input())
D = []
ans = 'No'
for i in range(N):
    D.append(list(map(int, input().split())))



for i in range(N-2):
    if D[i][0] == D[i][1]:
        if D[i+1][0] == D[i+1][1]:
            if D[i+2][0] == D[i+2][1]:
                ans = 'Yes'

print(ans)