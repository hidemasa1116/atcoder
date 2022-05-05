import collections
S = input()
c1 = collections.Counter(S)
ans = 'No'

if len(S) >= 3:
    for i in range(104, 1000, 8):
        i = str(i)
        if '0' not in i:
            c2 = collections.Counter(i)
            items = c2.items()
            flg = True
            for item in items:
                a = list(item)
                if c1[a[0]] < a[1]:
                    flg = False
            if flg:
                ans = 'Yes' 

elif len(S) == 2:
    s1 = int(S[0]+S[1])
    s2 = int(S[1]+S[0])
    if s1 % 8 == 0 or s2 % 8 == 0:
        ans = 'Yes'
else:
    if int(S) % 8 == 0:
        ans = 'Yes'


print(ans)

