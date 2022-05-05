# 13時ごろ開始

X, Y = map(int, input().split())

if Y <= X:
    print(0)
else:
    n = (Y - X) / 10
    if n == int(n):
        print(int(n))
    
    else:
        print(int(n+1))


