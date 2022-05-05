X = input()

if len(X) == 1:
    ans = 0
elif len(X) == 2 and X[0] == '-':
    ans = -1
else:
    A = X[:-1]
    B = X[-1]

    if int(A) < 0:
        if int(B) > 0:
            ans = int(A) -1
        else:
            ans = int(A)
    else:
        ans = int(A)

print(ans)



