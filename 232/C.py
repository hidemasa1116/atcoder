import itertools

N, M = map(int, input().split())
A, B, C, D = [], [], [], []

if M == 0:
    print('Yes')
    exit(0)


ans = 'No'

ab = [map(int, input().split()) for _ in range(M)]
A, B = [list(i) for i in zip(*ab)]

cd = [map(int, input().split()) for _ in range(M)]
C, D = [list(i) for i in zip(*cd)]

X = [i+1 for i in range(N)]

for x in list(itertools.permutations(X)):
    P = list(x)
    flg = 0
    
    for k in range(M):
        Pi = P[A[k]-1]
        Pj = P[B[k]-1]
        
        for l in range(M):
            if (C[l] == Pi and D[l] == Pj) or (C[l] == Pj and D[l] == Pi):
                flg += 1
                break

    if flg == M:
        ans = 'Yes'
            


print(ans)



