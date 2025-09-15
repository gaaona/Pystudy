import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
degrees = [0] * (N+1)
routes = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())

    routes[A].append(B)
    degrees[B] += 1

q = deque()

for i in range(1, N+1):
    if degrees[i] == 0:
        q.append(i)

ans = []

while q:
    now = q.popleft()
    ans.append(now)

    for route in routes[now]:
        degrees[route] -= 1
        if degrees[route] == 0:
            q.append(route)

print(*ans)
