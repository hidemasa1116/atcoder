N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

for i in range(N):
    n = A[i] // X
    if K >= n:
        K = K - n
        A[i] = A[i] - n*X
    else:
        A[i] = A[i] - K*X
        K = 0
        break

    
if K == 0:
    print(sum(A))

else:
    if K >= N:
        print(0) 

    else:
        A.sort(reverse=True)

        for i in range(K):
            A[i] = 0

        print(sum(A))











