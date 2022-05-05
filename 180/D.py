X, Y, A, B = map(int, input().split())
ans = 0

while X < Y:
    if X*A > Y and X+B > Y:
        break
        
    if X*A < Y and X*A <= X+B:
        X *= A
        ans += 1
    else:
        if (Y-X) % B == 0:
            ans += (Y-X) // B-1
        else:
            ans += (Y-X) // B
        break
    
print(ans)















# X, Y, A, B = map(int, input().split())
# score = 0

# def kako(x):
#     return x * A

# def at(x):
#     return x+B

# while X < Y:
#     if kako(X) >= at(X):
#         X = at(X)
#     else:
#         X = kako(X)
#     score += 1

# print(score-1)
    


