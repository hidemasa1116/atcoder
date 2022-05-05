from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))
D = defaultdict(list)

for i, x in enumerate(A, 1):
    D[x].append(i)

print(D)




xk = [map(int, input().split()) for _ in range(Q)]
x, k = [list(i) for i in zip(*xk)]



# for i in range(Q):
     
















