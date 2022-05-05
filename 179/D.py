N, K = map(int, input().split())
X = []
for i in range(K):
    L, K = map(int, input().split())
    X.append(L)
    X.append(K)

X = list(set(X))
X.sort(reverse=True)



