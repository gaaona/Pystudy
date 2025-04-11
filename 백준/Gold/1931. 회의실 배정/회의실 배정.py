N = int(input())
timetable = [0] * N


for i in range(N):
    start, end = map(int, input().split())
    timetable[i] = (end,start)

timetable.sort()

cnt = 0
end_time = 0

for time in timetable:
    if time[1]>= end_time:
        cnt += 1
        end_time = time[0]

print(cnt)