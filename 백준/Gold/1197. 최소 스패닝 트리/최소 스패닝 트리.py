import sys
import heapq

V, E = map(int, sys.stdin.readline().split())

routes = [[] for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())

    routes[A].append((C, B))
    routes[B].append((C, A))

visited = [False] * (V+1)
INF = 2147483648
distances = [INF] * (V+1)

pq = [(0,1)]
distances[0] = 0

ans = 0
cnt = 0

while pq:
    cost, node = heapq.heappop(pq)

    if visited[node]:
        continue

    visited[node] = True
    ans += cost
    cnt += 1

    if cnt == V:  # 모든 노드 연결 완료
        break

    for next_dist, next_node in routes[node]:
        if not visited[next_node]:
            heapq.heappush(pq,(next_dist, next_node))

print(ans)