from collections import deque

def bfs(i,j):
    global cnt, farm
    
    if visited[i][j] is True:
        return
    else:
        cnt += 1
        visited[i][j] = True

    q = deque()
    q.append((i,j))

    while q:
        ci, cj = q.popleft()
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni = di + ci
            nj = dj + cj

            if 0<=ni<N and 0<=nj<M and visited[ni][nj] is False:
                if farm[ni][nj] == 1:
                    q.append((ni,nj))
                    visited[ni][nj] = True
                else: # farm[ni][nj] == 0:
                    farm[ni][nj] = cnt
                    visited[ni][nj] = True


T = int(input())

for _ in range(T):
    M,N,K = map(int, input().split())

    farm = [[0] * M for _ in range(N)]

    for _ in range(K):
        m,n = map(int, input().split())

        farm[n][m] = 1

    cnt = 0
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if farm[i][j]:
                bfs(i,j)

    print(cnt)