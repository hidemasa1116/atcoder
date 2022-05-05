N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


a = [0]*N
a[0] = A[0]

b = [0]*N
b[0] = B[0]

ans = 'Yes'

# print('a:', a)
# print('b:', b)

for i in range(N-1):
    
    if a[i] != 0:
        if abs(a[i] - A[i+1]) <= K:
            a[i+1] = A[i+1]
        if abs(a[i] - B[i+1]) <= K:
            b[i+1] = B[i+1]
       
    
    if b[i] != 0:
        if abs(b[i] - A[i+1]) <= K:
            a[i+1] = A[i+1]
        if abs(b[i] - B[i+1]) <= K:
            b[i+1] = B[i+1]
    
    if a[i+1] == 0 and b[i+1] == 0:
        ans = 'No'
    
    # print('a:', a)
    # print('b:', b)

print(ans)














