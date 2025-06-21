import sys

T = int(input())

N = [int(sys.stdin.readline().rstrip()) for _ in range(T)]

m = max(N)

dp = [1] * (m+1)

for j in range(2,4):
    for i in range(1, m+1):
        if i >= j:
            dp[i] = dp[i] + dp[i - j]

for num in N:
    print(dp[num])