from collections import deque
from pprint import pprint

dirs = [(1,0,0), (-1,0,0), (0,0,1), (0,0,-1), (0,1,0), (0,-1,0)]

def find_nodes(matrix, L, R, C):
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if matrix[l][r][c] == 'S':
                    start = (l, r, c)
                elif matrix[l][r][c] == 'E':
                    end = (l, r, c)
    return start, end

def bfs(matrix, start, end, L, R, C): # S에서 E까지 가보기
    visited = [[[-1] * C for _ in range(R)] for _ in range(L)]
    q = deque()
    sl, sr, sc = start
    el, er, ec = end

    visited[sl][sr][sc] = 0
    q.append((sl, sr, sc))

    while q:
        l, r, c = q.popleft()

        if (l, r, c) == (el, er, ec):
            return visited[l][r][c]

        for dl, dr, dc in dirs:
            nl, nr, nc = l + dl, r + dr, c + dc
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                if visited[nl][nr][nc] == -1 and matrix[nl][nr][nc] != '#':
                    visited[nl][nr][nc] = visited[l][r][c] + 1
                    q.append((nl, nr, nc))

    return -1  # 출구에 도달 못함


while True:
    LRC = input().strip()
    if LRC == '':
        continue
    L, R, C = map(int, LRC.split())
    if (L, R, C) == (0, 0, 0):
        break

    matrix = []
    for _ in range(L):
        level = []
        while len(level) < R:
            row = input().strip()
            if row:
                level.append(list(row))
        matrix.append(level)

    start, end = find_nodes(matrix, L, R, C)
    result = bfs(matrix, start, end, L, R, C)

    if result == -1:
        print('Trapped!')
    else:
        print(f'Escaped in {result} minute(s).')

