S = input()
T = input()
count = 0
dif = []
ans = 'No'

# if sorted(S) == sorted(T):

#     for i in range(len(S)):
#         if S[i] != T[i]:
#             count += 1
#             dif.append(i)
#     print(count)
        
#     if count == 0:
#         ans = 'Yes'

#     elif count == 2:
#         if dif[1] - dif[0] == 1:
#             print(dif[1], dif[0])
#             ans = 'yes'
#         else:
#             ans = 'No'

#     else:
#         ans = 'No'

# else:
#     ans = 'No'


# print(ans)



#


if S == T:
    ans = 'Yes'

for i in range(len(S)-1):  
    Sl = list(S)
    Tl = list(T)
    Sl[i], Sl[i+1] = Sl[i+1], Sl[i]

    if Sl== Tl:
        ans = 'Yes'

print(ans)