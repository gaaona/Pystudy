di = [0,1,0,-1]
dj = [1,0,-1,0]


def f(i,j):
    stack = [(i,j)]
    visited = [[0] * 16 for _ in range(16)]
    visited[i][j] = 1

    while stack:
        pi, pj = stack.pop()

        for k in range(4):
            ni = pi + di[k]
            nj = pj + dj[k]

            if 0<=ni<16 and 0<=nj<16 and visited[ni][nj] == 0:
                if maze[ni][nj] == 0:
                    stack.append((ni,nj))
                    visited[ni][nj] = 1
                elif maze[ni][nj] == 3:
                    return True
    return False

def check():
    ans = 0

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                ans = f(i, j)

                if ans:
                    return 1
                else:
                    continue
    return 0

for _ in range(10):
    tc = int(input())

    maze = [list(map(int, input())) for _ in range(16)]

    res = check()
    print(f'#{tc} {res}')