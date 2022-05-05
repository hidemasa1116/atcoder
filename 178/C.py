import itertools

N = int(input())

ans = (10**N - 9**N - 9**N + 8**N) % (10**9 + 7)  

print(ans)


























# A = [i for i in range(10)]

# co = itertools.permutations(A, N)
# ans = 0

# for i in co:
#     j = list(i)
#     if 0 in j:
#         if 9 in j:
#             ans += 1

# print(ans)
