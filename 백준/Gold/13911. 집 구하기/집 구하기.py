import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, limit):
    visited = [INF] * (V+2)
    pq = [(0, start)]
    visited[start] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if visited[node] < dist:
            continue
        
        for next_node, next_dist in routes[node]:
            new_dist = dist + next_dist
            
            if new_dist <= limit and visited[next_node] > new_dist:
                visited[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

    return visited


V, E = map(int, input().split())

mc_dummy = 0
sb_dummy = V+1

routes = [[] for _ in range(V+2)]

for _ in range(E):
    u,v,w = map(int, input().split())
    routes[u].append((v,w))
    routes[v].append((u,w)) # 양방향

is_house = [True] * (V+2) # 집 여부
is_house[mc_dummy] = False
is_house[sb_dummy] = False

M, x = map(int, input().split())
mc_list = list(map(int, input().split()))

for mc in mc_list:
    routes[mc_dummy].append((mc, 0))
    is_house[mc] = False

S, y = map(int, input().split())
sb_list = list(map(int, input().split()))

for sb in sb_list:
    routes[sb_dummy].append((sb, 0))
    is_house[sb] = False

mc_map = dijkstra(mc_dummy, x)
sb_map = dijkstra(sb_dummy, y)

min_val = INF

for i in range(1, V+1):
    if is_house[i] and mc_map[i] <= x and sb_map[i] <= y: # 집이고 x와 y보다 가까운 경우
        min_val = min(min_val, mc_map[i] + sb_map[i])

if min_val == INF:
    print(-1)
else:
    print(min_val)
