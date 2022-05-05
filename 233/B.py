L, R = map(int, input().split())
S = input()

X = S[L-1:R]
X = X[::-1]

S = list(S)
X = list(X)

for i in range(L, R+1):
    S[i-1] = X[i-L]

print(''.join(S))





