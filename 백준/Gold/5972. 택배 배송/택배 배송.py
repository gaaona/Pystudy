import heapq

def dikstra(start_node):
    distances = [max_value] * (N+1)
    distances[start_node] = 0

    pq = [(0,start_node)]

    while pq:
        dist, node = heapq.heappop(pq)

        if dist < distances[node]:
            continue

        for next_info in routes[node]:
            next_dist = next_info[0]
            next_node = next_info[1]

            new_dist = dist + next_dist

            if distances[next_node] > new_dist:
                distances[next_node] = new_dist
                heapq.heappush(pq,(new_dist,next_node))

    return distances


N,M = map(int, input().split())

routes = [[] for _ in range(N+1)]

max_value = 2500000000
for _ in range(M):
    node1, node2, cows = map(int, input().split())

    routes[node1].append((cows,node2))
    routes[node2].append((cows,node1))

result = dikstra(1)

print(result[N])