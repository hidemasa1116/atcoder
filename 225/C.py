N, M = map(int, input().split())
B = []
ans = 'Yes'

for i in range(N):
    B.append(list(map(int, input().split())))

i = (B[0][0] // 7) + 1
j = B[0][0] % 7

if j == 0:
    if M != 1:
        ans ='No'

else:
    if j + M > 8:
        ans = 'No'    
    




for s in range(N):
    if M > 1:
        for l in range(M-1):
            if B[s][l+1] != B[s][l]+1:
                ans = 'No'
                break
            
    
    if s < N-1:
        if B[s+1][0] != B[s][0]+7:
            ans ='No'
            break

print(ans)





