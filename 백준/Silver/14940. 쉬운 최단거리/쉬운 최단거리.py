from collections import deque

# 델타
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 입력
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 방문 배열을 -1로 초기화
visited = [[-1] * M for _ in range(N)]

# 시작점 찾기 (2)
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            si, sj = i, j
            visited[i][j] = 0  # 시작점 거리 0
            break

# BFS
q = deque()
q.append((si, sj))

while q:
    i, j = q.popleft()
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        # 범위 내 & 방문 안 했고 & 도달 가능한 땅이면
        if 0 <= ni < N and 0 <= nj < M:
            if matrix[ni][nj] == 1 and visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))

# 도달 불가능한 부분 처리
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0: # 원래 0인 부분
            visited[i][j] = 0
        elif matrix[i][j] == 1 and visited[i][j] == -1: # 갈 수 있는데 못 간 땅
            visited[i][j] = -1
        # matrix[i][j] == 2인 위치는 이미 0으로 되어 있음

# 출력
for row in visited:
    print(*row)
