def f(idx,cnt, visited):
    global path

    if cnt == 6:
        print(*path)
        return

    if idx == k:
        return

    if k - idx < 6 - cnt:
        return

    for i in range(idx,k):
        if visited[i] == 0:
            visited[i] = 1
            path.append(nums[i])
            f(i+1,cnt+1, visited)
            visited[i] = 0
            path.pop()


import sys

while True:
    k, *nums = map(int, sys.stdin.readline().split())

    if k == 0:
        break

    path = []
    visited = [0] * k
    for i in range(k):
        path.append(nums[i])
        visited[i] = 1
        f(i+1,1,visited)
        visited[i] = 0
        path.pop()
    print()