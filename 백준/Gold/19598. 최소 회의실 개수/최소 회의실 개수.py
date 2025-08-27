import sys
import heapq

N = int(sys.stdin.readline().rstrip())
timetables = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    timetables.append((start, end))

timetables.sort() # 시작 시간 순서로 재정렬

occupations = [] # 끝나는 시간이 빠른 순서로 정렬
heapq.heappush(occupations, (0,0)) # 종료시간, 시작시간 순서

ans = 1

for start_time, end_time in timetables:
    if occupations[0][0] <= start_time: # 제일 빠른 종료 시간이 제일 빠른 시작 시간보다 빠른 경우(있는 회의실에서 회의 가능)
        heapq.heappop(occupations) # 삭제하고 회의실 갱신 할 거임
    else:
        ans += 1 # 회의실 이미 다 차서 그냥 새로운 회의실 쓸 거임
    heapq.heappush(occupations, (end_time, start_time))

print(ans)