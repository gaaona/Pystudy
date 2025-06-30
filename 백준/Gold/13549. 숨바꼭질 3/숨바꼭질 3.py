import heapq

def f(i, c):
    global arr

    q = []
    visited = [False] * 100001
    
    heapq.heappush(q, (c, i)) 
    visited[i] = True

    while q:
        cnt,idx = heapq.heappop(q) # 제일 횟수(cnt)가 적은 것부터 heappop

        if idx == K: # 젤 작은 cnt로 하기 때문에 제일 먼저 K된 cnt가 최솟값
            return arr[idx]
        
        if idx > 0 and visited[idx-1] == 0:
            arr[idx - 1] = min(arr[idx - 1],cnt+1)
            heapq.heappush(q,(cnt+1, idx-1))
            visited[idx-1] = True

        if idx*2 <= 100000 and visited[idx*2] == 0:
            arr[idx*2] = min(arr[idx*2],cnt)
            heapq.heappush(q,(cnt, idx * 2))
            visited[idx*2] = True
            
        if idx+1 <= 100000 and visited[idx+1] == 0:
            arr[idx+1] = min(arr[idx+1],cnt+1)
            heapq.heappush(q,(cnt+1,idx + 1))
            visited[idx+1] = True

N, K = map(int, input().split())
arr = [100002] * 100001 # max으로 초기화
arr[N] = 0

ans = f(N, 0)
print(ans)