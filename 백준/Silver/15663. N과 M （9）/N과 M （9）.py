def f(i, cnt):
    global results

    if cnt == M:
        print(*path)
        results.add(tuple(path)) # 중복 제거를 위해 set에 튜플로 저장
        return

    previous = None
    for j in range(N):
        if not visited[j] and nums[j] != previous: # 같은 숫자 연속 사용 방지
            visited[j] = True
            path.append(nums[j])
            f(i,cnt+1)
            path.pop()
            visited[j] = False
            previous = nums[j]


N,M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

path = []
visited = [False] * N
results = set()

for i in range(N):
    if i>0 and nums[i] == nums[i-1]:
        continue # 같은 숫자로 시작하는 경우 중복 방지
    visited[i] = True
    path.append(nums[i])
    f(i,1)
    path.pop()
    visited[i] = False
