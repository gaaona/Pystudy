from collections import deque

def bfs(start_node):
    ans = []
    visited = [0] * (N + 1)

    q = deque()
    q.append(start_node)

    while q:
        node = q.popleft()
        if visited[node]:
            continue
        ans.append(node)
        visited[node] = 1

        for x in routes[node]:
            if not visited[x]:
                q.append(x)
    return ans


def dfs(start_node):
    visited = [0] * (N + 1)
    ans = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if visited[node]:
            continue

        visited[node] = 1
        ans.append(node)

        # 스택이므로 순서를 뒤집어서 넣기
        for x in reversed(routes[node]):
            if not visited[x]:
                stack.append(x)
    return ans


N, M, V = map(int, input().split())

routes = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    routes[n1].append(n2)
    routes[n2].append(n1)

for i in range(1, N + 1):
    routes[i].sort()

dfs_ans = dfs(V)
bfs_ans = bfs(V)

print(*dfs_ans)
print(*bfs_ans)
