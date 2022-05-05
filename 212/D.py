import heapq

Q = int(input())
A = [list(map(int, input().split())) for i in range(Q)]
bag = []
heapq.heapify(bag)
ans = []
X = 0

for a in A:
    if a[0] == 1:
        heapq.heappush(bag, a[1])
    elif a[0] == 2:
        X += a[1]
    else:
        print(heapq.heappop(bag)+X)
        






