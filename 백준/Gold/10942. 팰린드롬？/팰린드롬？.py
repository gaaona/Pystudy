import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [[0] * N for _ in range(N)]

# 길이 1,2인 구간
for i in range(N - 1):
    dp[i][i] = 1
    if nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1
dp[N-1][N-1] = 1

# 길이 3 이상 구간에 대해 DP 채우기
for length in range(3, N + 1):
    for start in range(N - length + 1):
        end = start + length - 1
        if nums[start] == nums[end] and dp[start + 1][end - 1] == 1:
            dp[start][end] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    # 입력 인덱스가 1부터 시작하므로 0-based로 변환
    print(dp[S - 1][E - 1])
