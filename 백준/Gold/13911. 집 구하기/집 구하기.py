import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = 10**18

def dijkstra(start):
    visited = [INF] * (V+3)
    pq = [(0, start)]
    visited[start] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if visited[node] < dist:
            continue
        
        if routes[node]:
            for next_node, next_dist in routes[node]:
                if next_node == V+1 or next_node == V+2: # 더미데이터인 경우
                    continue

                new_dist = dist + next_dist
                
                if visited[next_node] > new_dist:
                    visited[next_node] = new_dist
                    heapq.heappush(pq, (new_dist, next_node))

    return visited


V, E = map(int, input().split())

routes = defaultdict(list)

for _ in range(E):
    u,v,w = map(int, input().split())
    routes[u].append((v,w))
    routes[v].append((u,w))

M, x = map(int, input().split())
mc_list = list(map(int, input().split()))

S, y = map(int, input().split())
sb_list = list(map(int, input().split()))

for mc in mc_list: # 모든 맥도날드에서의 최단 거리를 구하기 위한 더미 데이터
    routes[V+1].append((mc, 0))

for sb in sb_list: # 모든 스타벅스에서의 최단 거리를 구하기 위한 더미 데이터
    routes[V+2].append((sb, 0))

mc_map = dijkstra(V+1)
sb_map = dijkstra(V+2)

min_val = INF

for i in range(1, V+1):
    if i in mc_list or i in sb_list:
        continue
    if mc_map[i] <= x and sb_map[i] <= y:
        cnt = mc_map[i] + sb_map[i]
        if min_val > cnt:
            min_val = cnt

if min_val == INF:
    print(-1)
else:
    print(min_val)
