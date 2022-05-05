N = int(input())
X = []

for i in range(N):
    X.append(list(map(int, input().split())))

a = list(map(list, set(map(tuple, X))))
print(len(a))
