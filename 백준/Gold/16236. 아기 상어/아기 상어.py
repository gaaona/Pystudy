import sys
from collections import deque

input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def find_shark(): # 아기상어 첫 위치 찾기
    for i in range(1, N+1):
        for j in range(1, N+1):
            if matrix[i][j] == 9:
                return i,j
    
    return -1,-1


def bfs(si, sj):
    q = deque()
    q.append((si, sj))

    visited = [[-1]*(N+2) for _ in range(N+2)]
    visited[si][sj] = 0

    eat_list = []
    min_dist = None

    while q:
        x, y = q.popleft()

        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            
            # 범위 안인지(패딩 부분 아닌지) and 방문하지 않은 곳인지 and 상어가 지나갈 수 있는지
            if matrix[ni][nj] != -1 and visited[ni][nj] == -1 and matrix[ni][nj] <= shark_size:
                visited[ni][nj] = visited[x][y] + 1
                if 0 < matrix[ni][nj] < shark_size:
                    if min_dist is None or visited[ni][nj] == min_dist: # 첫 발견한 먹이 or 같은 최소거리에 있는 경우
                        eat_list.append((visited[ni][nj], ni, nj)) # 거리, 위, 왼쪽 기준
                        min_dist = visited[ni][nj]
                    elif visited[ni][nj] > min_dist: # 가장 가까운 거리보다 큰 경우는 볼 필요 없음
                        continue
                else:
                    q.append((ni, nj))
    if eat_list: # 먹을 수 있는 먹이가 있는지 확인
        eat_list.sort() # 거리, 위, 왼쪽 기준 정렬
        d, pi, pj = eat_list[0]
        return pi, pj, d
    return None


N = int(input().rstrip())

matrix = [[-1] * (N+2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)]  + [[-1] * (N+2)]
# 패딩을 넣어서 범위 내 조건 확인을 줄임

si, sj = find_shark()
matrix[si][sj] = 0

shark_size = 2
eat_count = 0
ans = 0

while True: # 가능한 먹이 다 먹을 때까지
    next_pos = bfs(si, sj)
    if not next_pos:
        break
    pi, pj, pd = next_pos

    ans += pd # 거리 == 걸린 시간
    si, sj = pi, pj

    eat_count += 1

    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

    matrix[pi][pj] = 0


print(ans)