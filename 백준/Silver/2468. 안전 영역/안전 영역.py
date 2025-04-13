from collections import deque

def bfs(i,j,v,cnt):
    global safe, max_cnt

    q = deque()
    safe[i][j] = cnt
    q.append((i,j))

    while q:
        pi, pj = q.popleft()

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni = pi + di
            nj = pj + dj

            if 0<=ni<N and 0<=nj<N and safe[ni][nj] is True:
                safe[ni][nj] = cnt
                q.append((ni,nj))

    if max_cnt < cnt:
        max_cnt = cnt


N = int(input())

min_v = 100
max_v = 0

map = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0

for i in range(N):
    for j in range(N):
        if min_v > map[i][j]:
            min_v = map[i][j]
        if max_v < map[i][j]:
            max_v = map[i][j]

for v in range(max_v):
    cnt = 0

    safe = [[True] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if map[i][j] <= v:
                safe[i][j] = False

    for i in range(N):
        for j in range(N):
            if safe[i][j] is True:
                cnt += 1
                bfs(i,j,v, cnt)
                

print(max_cnt)