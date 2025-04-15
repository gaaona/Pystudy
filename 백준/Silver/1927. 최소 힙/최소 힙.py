import sys
import heapq

N = int(sys.stdin.readline())

pq = []

for _ in range(N):
    tmp = 0
    num = int(sys.stdin.readline())
    if num == 0:
        if pq:
            tmp = heapq.heappop(pq)
        print(tmp)
    else:
        heapq.heappush(pq, num)
