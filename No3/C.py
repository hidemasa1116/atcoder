N = int(input())
A = list(map(int, input().split()))
X = int(input())

sum_A = sum(A)

n = X // sum_A
# for i in range(X+1):
#     if sum_A * i > X:
#         n = i-1
#         break

# n = 0
# for i in range(X+1):
#     if (X-i) % sum_A == 0:
#         n = (X-i) // sum_A
#         break


m = 0
count = 0
for i in range(len(A)):
    count += A[i]
    if count > X - sum_A*n:
        m = i+1
        break

print(N*n + m)




