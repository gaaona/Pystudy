import sys

N,M = map(int, sys.stdin.readline().split())

routes = [[] for _ in range(N+1)]

for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    routes[node1].append(node2)
    routes[node2].append(node1)

visited = [0] * (N+1)
group = 0
for i in range(1,N+1):
    if routes[i] and visited[i] == 0:
        group += 1
        stack = [i]

        while stack:
            node = stack.pop()

            if visited[node] == 0:
                visited[node] = group

                for next_node in routes[node]:
                    stack.append(next_node)
    elif visited[i] == 0:
        group += 1
        visited[i] = group

print(group)