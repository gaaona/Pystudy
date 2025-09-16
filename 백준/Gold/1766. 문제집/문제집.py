import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
routes = [[] for _ in range(N+1)]
degrees = [0] * (N+1)

for _ in range(M):
    A,B = map(int, input().split())
    routes[A].append(B)
    degrees[B] += 1

pq = []

for i in range(1, N+1):
    if degrees[i] == 0:
        heapq.heappush(pq, i)

while pq:
    now = heapq.heappop(pq) # 지금 차수가 제일 작은 수

    print(now, end=" ")
    for route in routes[now]:
        degrees[route] -= 1
        if degrees[route] == 0:
            heapq.heappush(pq, route)