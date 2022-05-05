n = list(map(int, input().split()))
A = n[0]
B = n[1]
C = n[2]

ans = -1

for i in range(1, B+1):
    if C * i >= A and C * i <= B:
        ans = C * i
        break

print(ans)
    