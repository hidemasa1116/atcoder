alp = []
P = list(map(int, input().split()))

for i in range(97, 123):
    alp.append(chr(i))

for i in P:
    print(alp[i-1], end='')

