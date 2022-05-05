N, X = map(int, input().split())
S = list(input())
T = []

# i = 0
# j = 0
# while i < N-1:
#     if (S[j] == 'L' or S[j] == 'R') and S[j+1] == 'U':
#         del S[j:j+2]
#     else:
#         j += 1
#         i += 1

#     i += 1


for i in S:
    if i == 'U' and len(T) > 0 and (T[-1] == 'R' or T[-1] == 'L'):
        T.pop()
    else:
        T.append(i)


for i in T:
    if i == 'U':
        X = X // 2
    
    elif i == 'L':
        X = X * 2
    elif i == 'R':
        X = X * 2 + 1

print(int(X))



