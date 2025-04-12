N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True) # 큰 동전 순으로 골라야 동전 수가 적으니까 역순 정렬

ans = 0

for coin in coins:
    if K>=coin: # 금액이 동전 크기보다 큰 경우(동전으로 나눌 수 있는 경우)
        ans += K//coin # 정답에 나눈 몫을 더함
        K%=coin # 금액을 나눠서 나머지로 만듦

print(ans)