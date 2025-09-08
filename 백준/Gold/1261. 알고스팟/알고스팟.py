import sys
import heapq

input = sys.stdin.readline

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

M, N = map(int, input().split())
matrix = [input().rstrip() for _ in range(N)]

INF = 10001 # 가로100*세로100 보다 큰 수
visited = [[INF] * M for _ in range(N)]

q = []
heapq.heappush(q, (0, 0, 0)) # 부순 벽 수, 행, 열
visited[0][0] = 0 # 시작이니까 초기화

while q:
    cnt, i, j = heapq.heappop(q)

    for di, dj in directions:
        ni, nj = di + i, dj + j

        if 0 <= ni < N and 0 <= nj < M:
            if matrix[ni][nj] == '1': # 벽인 경우
                next_cnt = cnt + 1 # 벽 세기 하나 추가
            else:
                next_cnt = cnt # 벽 세기 추가 X 그대로 cnt

            if visited[ni][nj] == INF or visited[ni][nj] > next_cnt: # 방문한 적 없거나 지금이 더 부순 수가 적으면
                visited[ni][nj] = next_cnt
                heapq.heappush(q, (visited[ni][nj], ni, nj))

print(visited[N - 1][M - 1])