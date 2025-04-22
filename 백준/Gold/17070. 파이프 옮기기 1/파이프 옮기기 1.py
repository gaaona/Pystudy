import sys

N = int(sys.stdin.readline())

wall = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1 # [i][j][d]

# 0:가로 1:세로 2:대각선

for i in range(N):
    for j in range(N):
        if wall[i][j] == 1: # 막혀있으면
            continue

        if j-1>=0: # 가로 가능 여부 확인
            dp[i][j][0] += (dp[i][j - 1][0] + dp[i][j - 1][2])

        if i-1>=0: # 세로 가능 여부 확인
            dp[i][j][1] += (dp[i - 1][j][1] + dp[i - 1][j][2])

        if i-1>=0 and j-1>=0: # 대각선 가능 여부 확인
            if wall[i-1][j] == 0 and wall[i][j-1] == 0: # 가로 세로도 비어있는지
                dp[i][j][2] += (dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2])


print(sum(dp[N-1][N-1]))