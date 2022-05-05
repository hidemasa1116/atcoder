
N = int(input())
Z = [input().split() for i in range(N)]
ans = []

for i in Z:
    for j in Z:
        for k in Z:
            a = [i, j, k]
            a1 = sorted(a)
            if a1 not in ans:
                if a1[0] != a1[1] and a1[0] != a1[2] and a1[1] != a1[2]:
                    n = int(a1[1][1])-int(a1[0][1])
                    m = int(a1[1][0])-int(a1[0][0])
                    l = int(a1[2][1])-int(a1[0][1])
                    s = int(a1[2][0])-int(a1[0][0])
                    if m == 0 and s == 0:
                        pass
                    elif m == 0 or s == 0:
                        ans.append(a1)
                    else:
                        if n / m != l / s:
                            ans.append(a1)

            
                    
                      
print(len(ans))


            





