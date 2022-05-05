import itertools
S = input()
a = S[0]
b = S[1]
c = S[2]

l = len(list(set([a, b, c])))

if l == 1:
    print(1)
elif l == 2:
    print(3)
else:
    print(6)






