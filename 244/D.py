S = list(map(str, input().split()))
T = list(map(str, input().split()))

X = [['R', 'G', 'B'], ['G', 'B', 'R'], ['B', 'R', 'G']]
Y = [['R', 'B', 'G'], ['G', 'R', 'B'], ['B', 'R', 'G']]

if S in X:
    if T in X:
        ans = 'Yes'
    else:
        ans = 'No'

else:
    if T in X:
        ans = 'No'
    else:
        ans = 'Yes'

print(ans)





























# if T == ['R', 'G', 'B']:
#     ans = 'Yes'
# elif T == ['R', 'B', 'G']:
#     ans = 'No'

# elif T == ['G', 'R', 'B']:
#     ans = 'No'
# elif T == ['G', 'B', 'R']:
#     ans = 'Yes'

# elif T == ['B', 'R', 'G']:
#     ans = 'Yes'
# elif T == ['B', 'G', 'R']:
#     ans = 'No'

# print(ans)






