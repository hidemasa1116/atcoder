def Yes():
    print('Yes')
    exit(0)

N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
X, Y = [list(i) for i in zip(*xy)]
S = input()

right_min, left_max = dict(), dict()

for i in range(N):
    if S[i] == 'R':
        if Y[i] in left_max and X[i] < left_max[Y[i]]:
            Yes()
    
    if S[i] == 'L':
        if Y[i] in right_min and X[i] > right_min[Y[i]]:
            Yes()



    if S[i] == 'R':
        if Y[i] in right_min:
            right_min[Y[i]] = min(X[i], right_min[Y[i]]) 
        else:
            right_min[Y[i]] = X[i]
    
    if S[i] == 'L':
        if Y[i] in left_max:
            left_max[Y[i]] = max(X[i], left_max[Y[i]])
        else:
            left_max[Y[i]] = X[i]

print('No')

