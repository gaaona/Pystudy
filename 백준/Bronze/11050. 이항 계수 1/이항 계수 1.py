N, K = map(int,input().split())

ans = 1

for n in range(N,N-K,-1):
    ans *= n

for k in range(K, 1,-1):
    ans /= k

print(int(ans)) # 자연수 N과 정수 K의 조합의 수는 항상 정수임