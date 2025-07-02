from collections import deque

dn = [0, 1, 0, -1, 0, 0] # 행
dm = [0, 0, 1, 0, -1, 0] # 열
dh = [1, 0, 0, 0, 0, -1] # 층


def find_first_tomatoes(): # 처음 토마토가 있는 자리들
    global q, visited

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if matrix[i][j][k] == 1: # 초기 익은 토마토 있는 칸
                    q.append((i, j, k)) # deque에 넣기
                    visited[i][j][k] = 0 # 방문 표시
                elif matrix[i][j][k] == -1: # 토마토 없는 칸
                    visited[i][j][k] = 0 # 방문 표시


def find_answer():
    res = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if visited[i][j][k] == -1: # 토마토 있는 칸인데 방문 안 한 칸
                    return -1 
                elif visited[i][j][k] > res: # 완탐하는 김에 최대 일수 세기
                    res = visited[i][j][k]
    return res 


M, N, H = map(int, input().split())

matrix = [[[] for _ in range(N)] for _ in range(H)]

for h in range(H - 1, -1, -1): # 가장 밑에 층부터 주기 때문에 역순
    for n in range(N): # 층 별로는 또 순서대로
        new_row = list(map(int, input().split()))
        matrix[h][n] = new_row

q = deque()
visited = [[[-1] * M for _ in range(N)] for _ in range(H)] 

find_first_tomatoes() # 초기 배치 확인

while q:
    h, n, m = q.popleft()

    for r in range(6):
        nh, nn, nm = h + dh[r], n + dn[r], m + dm[r] # 주변 토마토 좌표

        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and visited[nh][nn][nm] == -1: # 범위 안이고 방문 안 한 토마토면 
            visited[nh][nn][nm] = visited[h][n][m] + 1 # 영향 받은 토마토보다 하루 추가
            q.append((nh, nn, nm)) # 다음 영향력 토마토 목록에 추가

ans = find_answer()
print(ans)