N = int(input())
A = list(map(int, input().split()))
X = {}

for i in range(len(A)):
    X[i+1] = A[i]

A.sort(reverse=True)
ans = A[1]
ans1 = [k for k, v in X.items() if v == ans]

for i in ans1:
    print(i)


# X_sorted = sorted(X.items(), key=lambda x:x[1])

# print(X_sorted[])




