a, b, c, d = map(int, input().split())

n = a*c
m = a*d
s = b*c
l = b*d

print(max(n, m, s, l))



