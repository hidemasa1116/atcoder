N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def No():
    print('No')
    exit(0)

for i in range(M):
    if B[i] in A:
        A.remove(B[i])
    else:
        No()

print('Yes')

