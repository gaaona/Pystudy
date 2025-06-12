def f(i, cnt):
    global path

    if cnt == M:
        print(*path)
        return
    for k in range(i, N+1):
        path.append(k)
        f(k, cnt+1)
        path.pop()

N, M = map(int, input().split())

path = []

for i in range(1,N+1):
    path.append(i)
    f(i, 1)
    path.pop()
