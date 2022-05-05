import bisect
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()


ans = abs(A[0]-B[0])

for a in A:
    if a >= B[M-1]:
        ans = min(ans, abs(a-B[M-1]))
    elif a <= B[0]:
        ans = min(ans, abs(a-B[0]))
    else:
        index = bisect.bisect_left(B, a)
        ans = min(ans, abs(a-B[index]), abs(a-B[index-1]))


print(ans)




