import sys

def f(cnt):
    global path, visited

    if cnt == M:
        print(*path)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            path.append(nums[i])
            f(cnt+1)
            path.pop()
            visited[i] = 0


N, M = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

path = []
visited = [0] * N

f(0)