N = int(input())

dp = [[0] * (N+1) for _ in range(2)]

for i in range(3, N+1):
    if i%5 == 0:
        dp[0][i] = i//5
    if i%3 ==0:
        dp[1][i] = i//3

number = N
cnt = 0
min_cnt = 5000

for j in range(3, N+1):
    number = N
    if dp[0][j]:
        number -= j
        cnt = dp[0][j]

        if (number == 0 and j == N) or (3 <= number <= N and dp[1][number]):
            cnt += dp[1][number]
            if min_cnt > cnt:
                min_cnt = cnt

if min_cnt == 5000:
    if dp[1][N]:
        print(dp[1][N])
    else:
        print(-1)
else:
    print(min_cnt)