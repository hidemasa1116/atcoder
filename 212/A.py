A, B = map(int, input().split())

if A == 0:
    ans = 'Silver'
elif B == 0:
    ans = 'Gold'
else:
    ans = 'Alloy'

print(ans) 