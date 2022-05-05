# import math

# N = int(input())
# m = int(math.log2(N))

# print(m)


N = int(input())

k = 0
while 2**(k+1) <= N:
    k += 1
    

print(k)

