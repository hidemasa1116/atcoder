# PyPyの場合、MODのような定数はグローバルに置いたほうがやや速いらしい？
# Pythonはローカルに置いたほうが速い

MOD = 998244353  # 問題文からコピペするか、テンプレに10**9+7と一緒に入れとくといいです


def solve():
    N = int(input())
    dp = [[0] * 11 for _ in range(N + 1)]  # 0~10があることにする
    print(dp)

    for i in range(1, 10):
        dp[1][i] = 1  # 上から1桁目の1～9はそれぞれ1通り
    print(dp)    
    
    for i in range(1, N):
        for j in range(1, 10):
            dp[i + 1][j] = (dp[i][j - 1] + dp[i][j] + dp[i][j + 1]) % MOD
    print(dp)

    return sum(dp[N]) % MOD


print(solve())
