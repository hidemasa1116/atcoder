a, b = map(int, input().split())


if abs(a - b) == 1:
    ans = 'Yes'
else:
    if abs(a - b) == 9:
        ans = 'Yes'
    else:
        ans = 'No'

print(ans)

