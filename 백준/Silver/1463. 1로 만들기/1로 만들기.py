N = int(input())

dp = [0] * (N+1) # N번 인덱스가 있는 만큼... 0번 인덱스는 안 쓴다

for i in range(2,N+1):
    dp[i] = dp[i-1] + 1 # 실시간 업뎃 +1이 젤 크니까 우선 해놓기...
    
    if i%3 == 0: # 3으로 나눠지면
        dp[i] = min(dp[i//3]+1, dp[i]) # 둘 중에 작은 거
    if i%2 == 0: # 2로 나눠지면
        dp[i] = min(dp[i//2]+1, dp[i]) # 둘 중에 작은 거

print(dp[N]) # N에 도착하는 최소값