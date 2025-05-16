import sys

N,M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(trees)
max_height = 0

while left<=right:
    m = (left + right) // 2

    cnt = 0
    for tree in trees:
        if tree>m:
            cnt += (tree - m)
            
    if cnt<M:
        right = m -1
    else:
        max_height = max(max_height, m)
        left = m + 1

print(max_height)
