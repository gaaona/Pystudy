import sys
import heapq

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    min_pq = []
    max_pq = []

    k = int(input().rstrip())
    is_available = [False] * k # pq가 두 개라 어느 한 쪽에서라도 삭제됐는지 확인하는 배열

    for i in range(k):
        command, num = input().split()
        num = int(num)
        
        if command == 'I': 
            heapq.heappush(min_pq, (num, i)) # 양 쪽에 다 삽입
            heapq.heappush(max_pq, (-num, i)) # 양 쪽에 다 삽입
            is_available[i] = True # 
        elif command == 'D': 
            if num == -1: # 최소값 삭제
                while min_pq:
                    tmp, idx = heapq.heappop(min_pq)
                    if is_available[idx]: # 삭제되지 않은 idx인 경우
                        is_available[idx] = False # 삭제
                        break
                    else: # 삭제된 경우
                        continue # 삭제할 거 찾으러 계속
            elif num == 1: # 최대값 삭제
                while max_pq:
                    tmp,idx = heapq.heappop(max_pq)
                    if is_available[idx]: # 삭제되지 않은 idx인 경우
                        is_available[idx] = False # 삭제
                        break
                    else:
                        continue

    INF = 2**32
    min_val = max_val = INF
    while max_pq:
        tmp,idx = heapq.heappop(max_pq)
        if is_available[idx]:
            max_val = -tmp
            break
        else:
            continue
    while min_pq:
        tmp,idx = heapq.heappop(min_pq)
        if is_available[idx]:
            min_val = tmp
            break
        else:
            continue
    
    if min_val == INF or max_val == INF:
        print("EMPTY")
    else:
        print(max_val,min_val)