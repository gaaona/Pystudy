import sys

N, K = map(int, sys.stdin.readline().split())
items = [0] * (N+1)
for i in range(1,N+1):
    W,V = map(int, sys.stdin.readline().split())
    items[i] = (W,V)

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1,K+1):
        if j>=items[i][0]: # 배낭에 넣을 수 있으면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i][0]]+items[i][1])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[N][K])