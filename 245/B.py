N = int(input())
A = list(map(int, input().split()))

A.sort()
num = 0

for i in A:
    if i > num:
        break

    elif i == num:
        num += 1
    
print(num)





