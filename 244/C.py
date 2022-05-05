N = int(input())

ans = [i for i in range(1, 2*N+2)]

n = 100

while n != 0:

    print(ans[0])
    ans.remove(ans[0])

    n = int(input())
    if n != 0:
        ans.remove(n)
    
    








