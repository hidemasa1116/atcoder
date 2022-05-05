S, T, X = map(int, input().split())

ans = 'No'

if S < T:
    if (S <= X) and (X < T):
        ans = 'Yes'
else:
    if (X < T) or (S <= X):
        ans = 'Yes'

print(ans)

