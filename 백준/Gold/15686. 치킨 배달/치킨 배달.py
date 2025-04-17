def f(idx,cnt,visited):
    global min_sum, survived

    if cnt == M:
        total = count_dist(survived)

        min_sum = min(min_sum, total)
        return

    for i in range(idx,C):
        if visited[i] == 1:
            continue
        visited[i] = 1
        survived[cnt] = chicken[i]
        f(i+1,cnt+1,visited)
        visited[i] = 0



def count_dist(path):
    total = 0
    for hi, hj in house:
        cnt = 13000
        for i in range(M):
            ci, cj = path[i]
            cnt = min(cnt,(abs(hi - ci) + abs(hj - cj)))
        total += cnt
    return total


N, M = map(int,input().split())
city_map = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city_map[i][j] == 1:
            house.append((i,j))
        elif city_map[i][j] == 2:
            chicken.append((i,j))

C = len(chicken)
survived = [0] * M

min_sum = 13000
if C == M:
    min_sum = count_dist(chicken)
else:
    for i in range(C-M+1):
        visited = [0] * C
        f(i,0,visited)
            # print(min_sum)
print(min_sum)