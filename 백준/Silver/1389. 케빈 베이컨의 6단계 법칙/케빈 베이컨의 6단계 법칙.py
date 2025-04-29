from collections import deque

def bfs(from_person, to_person):
    visited = [0] * (N + 1)
    visited[from_person] = 1
    q = deque([from_person])

    while q:
        current = q.popleft()

        if current == to_person:
            return visited[current] - 1

        for neighbor in friends[current]:
            if visited[neighbor] == 0:
                visited[neighbor] = visited[current] + 1
                q.append(neighbor)
    return 0



N,M = map(int, input().split())

friends = [[] for _ in range(N+1)]

for _ in range(M):
    friend1, friend2 = map(int, input().split())

    friends[friend1].append(friend2)
    friends[friend2].append(friend1)

bacon = [500000] * (N+1)

for from_person in range(1,N+1):
    total = 0
    for to_person in range(1, N + 1):
        if to_person == from_person:
            continue

        total += bfs(from_person, to_person)
    bacon[from_person] = total

print(bacon.index(min(bacon)))