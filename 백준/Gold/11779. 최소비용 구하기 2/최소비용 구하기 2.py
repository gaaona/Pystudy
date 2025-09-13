import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)

def dijkstra(start):
    distance = [INF] * (N+1)
    prev = [[] for _ in range(N+1)]
    pq = [(0, start)]
    distance[start] = 0

    while pq:
        dist, node = heapq.heappop(pq)
        if distance[node] < dist:
            continue
        for next_node, next_dist in routes[node]:
            new_dist = dist + next_dist
            if distance[next_node] > new_dist:
                distance[next_node] = new_dist
                prev[next_node] = node
                heapq.heappush(pq, (new_dist, next_node))
    return distance, prev

N = int(input().rstrip())
M = int(input().rstrip())
routes = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    routes[s].append((e, w))

S, G = map(int, sys.stdin.readline().split())
distance, prev = dijkstra(S)

# 경로 복원
path = []
current = G
while current:
    path.append(current)
    current = prev[current]
path.reverse()

print(distance[G])
print(len(path))
print(*path)
