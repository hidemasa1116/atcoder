import itertools
S = input()
ans = 0

P = itertools.permutations(S, 8)

for p in P:
    if p == ('c', 'h', 'o', 'k', 'u', 'd', 'a', 'i'):
      ans += 1

print(ans)
    



