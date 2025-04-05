import sys

N,M = map(int, sys.stdin.readline().split())

nums=list(map(int,sys.stdin.readline().split()))
prefixed = [0] * (N+1)

for i in range(1,N+1):
    prefixed[i] = prefixed[i-1] + nums[i-1]

for _ in range(M):
    s,e = map(int, sys.stdin.readline().split())
    print(prefixed[e]-prefixed[s-1])