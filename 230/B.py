S = input()
T = 'oxx' * (10**5)

ans = 'No'

for i in range(len(T)):
    
    if i <= len(T)-len(S):

        flg = 0

        for j in range(len(S)):
            if T[i+j] != S[j]:
                flg = 1
                break
        
        if flg == 0:
            ans = 'Yes'
            break

print(ans)













