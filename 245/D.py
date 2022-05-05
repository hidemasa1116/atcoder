import numpy
N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

a = numpy.poly1d(A[::-1])
c = numpy.poly1d(C[::-1])

b = c/a
ans = b[0].coef

ans_list = []

for x in reversed(ans):
    ans_list.append(int(x))


print(*ans_list)






# B = [0] * (N+M+1)

# for i in range(N+1):
#     for j in range(M+1):
#         C[(N+M) - (i+j)] += A[N-i] + 










