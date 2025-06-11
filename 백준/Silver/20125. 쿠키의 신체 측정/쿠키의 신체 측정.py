def find_heart():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == "*":
                return i+1, j

N = int(input())
matrix = [input() for _ in range(N)]

heart = []

di = [0, 0, 1]
dj = [-1, 1, 0]
d = -1

li = [1, 1]
lj = [-1,1]
ld = -1

si,sj = find_heart() # 심장을 기준으로 양 팔과 몸통 길이를 잴 거임
print(si+1, sj+1)

ni = nj = 0
for _ in range(3): # 팔이랑 몸통 길이 재는 for문
    d += 1
    cnt = 0
    ni, nj = si+ di[d], sj+ dj[d] # 심장 외의 첫 신체부위 좌표로 재할당
    while 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == "*":
        cnt += 1
        ni, nj = ni + di[d], nj + dj[d]

        if (ni,nj) == (si,sj): # 심장을 만나면(팔 이슈 해결용)
            break
    print(cnt, end=' ')


ti, tj = (ni-1), nj # 엉덩이 (몸통 끝나는 부분)으로 선언
for _ in range(2): # 다리 길이 재는 for문
    ld += 1
    ni, nj = ti + li[ld], tj + lj[ld] # 다리 첫 부분으로 재할당
    cnt = 0
    while 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == "*":
        cnt += 1
        ni,nj = ni + di[d], nj + dj[d]
    print(cnt, end=' ')