N = int(input())
X = list(map(int, input().split()))

m = 0
for i in X:
    m += abs(i)

u2 = 0
for i in X:
    u2 += (abs(i))**2
u = (u2)**(0.5)

t_list = []
for i in X:
    t_list.append(abs(i))
t = max(t_list)

print(m)
print(u)
print(t)

