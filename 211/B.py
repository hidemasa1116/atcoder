S1 = input()
S2 = input()
S3 = input()
S4 = input()

ans = [S1, S2, S3, S4]
ans_set = set(ans)

if len(ans_set) == 4:
    print('Yes')
else:
    print('No')
