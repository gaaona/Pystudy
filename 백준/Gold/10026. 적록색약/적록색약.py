import sys
from collections import deque

input = sys.stdin.readline

# 적녹색약용 컬러맵
color_map = {
    'R' : ('R', 'G'),
    'G' : ('R', 'G'),
    'B' : ('B')
}

# 델타 탐색용
di = [0,1,0,-1]
dj = [1,0,-1,0]


def bfs(i,j, cnt, is_colormap, visited):
    stack = deque()
    stack.append((i,j))
    
    # 적녹색약 탐색 여부에 따라 컬러맵 지정
    if is_colormap:
        colormap = color_map[matrix[i][j]]
    else:
        colormap = matrix[i][j]

    while stack:
        ti,tj = stack.popleft()

        for d in range(4):
            ni = ti + di[d]
            nj = tj + dj[d]
            
            # 범위 안에 있고 방문하지 않았고 컬러맵 안의 색인지 확인
            # 적녹색약 탐색인 경우 R,G는 같은 그룹으로 계산하고 아닌 경우 다르게 계산하기 위함
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and matrix[ni][nj] in colormap:
                stack.append((ni,nj))
                visited[ni][nj] = cnt


N = int(input())
matrix = [list(input().rstrip()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
visited_two_color = [[False] * N for _ in range(N)] # 적녹색약 탐색용 visited

cnt = 0
cnt_two_color = 0 # 적녹색약 탐색용

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt += 1
            bfs(i,j, cnt, False, visited)
        if not visited_two_color[i][j]: # 적녹색약 탐색용
            cnt_two_color += 1
            bfs(i,j,cnt_two_color, True, visited_two_color)

print(cnt, cnt_two_color)