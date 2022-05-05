import copy

N, K = map(int, input().split())
P = []
for i in range(N):
    p = list(map(int, input().split()))
    n = sum(p)
    P.append(n)

P_sorted = sorted(P, reverse=True)

P_sort = copy.copy(P_sorted)


for i in range(N):
    P_sorted.remove(P[i])
    if P[i]+300 >= P_sorted[K-1]:
        print('Yes')
    else:
        print('No')
    P_sorted = copy.copy(P_sort)
    
    
 





# P = [list(map(int, input().split())) for i in range(N)]


# for i in range(N):
#     n = sum(P[i])





