N = int(input())
X = []
Y = [i for i in range(1, N+1)]


for i in range(N-1):
    X.append(list(map(int, input().split())))

for i in range(N-1):
    Y = set(Y) & set(X[i])

if len(list(Y)) >= 1:
    print('Yes')
else:
    print('No')




