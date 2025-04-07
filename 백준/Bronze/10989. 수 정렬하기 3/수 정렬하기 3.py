import sys

N = int(sys.stdin.readline())

counts = [0] * 10001

for _ in range(N):
    counts[int(sys.stdin.readline())] += 1

cnt = 0
for i in range(1,10001):
    if counts[i]:
        n = counts[i]
        cnt += n
        for _ in range(n):
            print(i)

        if cnt == N:
            break