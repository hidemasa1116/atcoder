S1 = input()
S2 = input()
S3 = input()
T = str(input())

ans = ''

for i in range(len(T)):
    if T[i] == '1':
        ans = ans + S1
    if T[i] == '2':
        ans = ans + S2
    if T[i] == '3':
        ans = ans + S3

print(ans)


