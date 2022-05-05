import itertools
N = int(input())
X = [list(map(int, input().split())) for i in range(N)]

Y = list(itertools.combinations(X, 3))
ans = 'No'


for i in Y:
    y = list(i)
    z = sorted(y)
    if z[1][0] == z[0][0]:
        if z[1][1] == z[0][1]:
            ans = 'Yes'
        else:
            if z[2][0] == z[0][0]:
                ans = 'Yes'
    else:
        r1 = (z[1][1]-z[0][1]) / (z[1][0]-z[0][0])
        if z[2][0] == z[0][0]:
            if z[2][1] == z[0][1]:
                ans ='Yes'
        else:
            r2 = (z[2][1]-z[0][1]) / (z[2][0]-z[0][0])
            if r1 == r2:
                ans ='Yes'
    

print(ans)

        
    


