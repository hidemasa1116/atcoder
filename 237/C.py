S = input()
N = len(S)

# ans = 0
# for i in range(N):
#     if S[i] != S[N-1-i]:
#         ans = 1
    
# if ans == 0:
#     print('Yes')
# else:
i = 1
while S[-i] == 'a':
    i += 1
right = i-1

j = 0
while S[j] == 'a':
    j += 1
left = j

n = right - left
S = 'a'*n + S

ans = 0
for i in range(N+n):
    if S[i] != S[N+n-1-i]:
        ans = 1
if ans == 0:
    print('Yes')
else:
    print('No')



































# S = input()
# N = len(S)

# ans = 'Yes'
# for i in range(N):
#     if S[i] != S[N-1-i]:
#         ans = 'No'    
# if ans == 'Yes':
#     print(ans)
#     exit(0)


# ans = 'Yes'
# for j in range(1, 10**6):
#     S = 'a' + S
#     for i in range(N+j):
#         if S[i] != S[N+j-1-i]:
#             ans = 'No'  
# if ans == 'Yes':
#     print(ans)
#     exit(0)

# print('No')


























