# import math

# N = int(input())
# count_A = 0
# count_B = 0

# n = N
# while True:
#     if((n&(n-1)) == 0):
#         max_2 = n
#         break
#     else:
#         n = n-1

# count_A = N - n
# count_B = int(math.log2(n))



N = int(input())
X = 1
count_A = 0
count_B = 0

while X * 2 <= N:
    X = X * 2
    count_B += 1

count_A = N - X + 1

print('A', end = '')
for i in range(count_B):
    print('B', end = '')
for i in range(count_A):
    print('A', end = '')