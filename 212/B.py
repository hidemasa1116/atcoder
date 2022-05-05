X = input()
A = [int(i) for i in X]
ans = 'Weak'

if A[0] == A[1] == A[2] == A[3]:
    ans = 'Weak'
else:
    for i in range(3):
        if A[i] == 9:
            if A[i+1] != 0:
                ans = 'Strong'
        else:
            if A[i+1] != A[i]+1:
                ans ='Strong'



print(ans)
