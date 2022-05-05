INF = 1 << 60

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

dp = [[-INF] * W for _ in range(H)]
dp[0][0] = 1

print(dp)

for row in range(H):
    for col in range(W):

        if row == col == 0:
            continue

        if C[row][col] == ".":
            d1 = dp[row - 1][col] if row - 1 >= 0 else -INF
            d2 = dp[row][col - 1] if col - 1 >= 0 else -INF
            dp[row][col] = max(d1, d2) + 1

ans = 0

for dp_row in dp:
    ans = max(ans, *dp_row)

print(ans)























# H, W = map(int, input().split())
# C = [list(input()) for _ in range(H)]

# flg = 0
# pos = [[0, 0]]
# while flg == 0:

#     for p in pos:
#         i = p[0]
#         j = p[1]
        

#         if i < H-1:
#             if C[i+1][j] == '.':
#                 pos.append([i+1, j])

#         if j < W-1:
#             if C[i][j+1] == '.':
#                 pos.append([i, j+1])

#         if len(pos) > 1:
#             pos.pop(0)
#         else:
#             print(pos[0][0] + pos[0][1] + 1)
#             flg = 1


    













