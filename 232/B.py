S = list(input())
T = list(input())
A = []
ans = 'No'

for i in range(97, 123):
    A.append(chr(i))

A = A + A

for i in range(26):
    flg = 0
    for j in range(len(S)):
        if A[A.index(S[j]) + i] != T[j]:
            flg = 1
            break
        
    if flg == 0:
        ans = 'Yes'

print(ans)

