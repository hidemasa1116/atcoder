from itertools import permutations
S, K = input().split()
K = int(K)
st = set()

for i in permutations(S):
    st.add(''.join(i))

ans = sorted(st)

print(ans[K-1])
