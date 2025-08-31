import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    times = [0] + list(map(int, sys.stdin.readline().split()))
    rules = [[] for _ in range(N+1)]
    degree = [0] * (N+1) # 위상 정렬을 지키기 위한 진입 차수

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        rules[x].append(y)
        degree[y] += 1
    
    W = int(sys.stdin.readline().rstrip())
    # 입력값 정리 끝
    
    # 누적값 계산
    dp = [0] * (N+1)
    q = deque()

    for i in range(1, N+1): # 0번 위상 찾기
        if degree[i] != 0: # 아직 사전 단계 남음(진입 불가)
            continue
        else:
            q.append(i)
            dp[i] = times[i]
    
    while q:
        building_now = q.popleft()

        for next_building in rules[building_now]:
            degree[next_building] -= 1
            dp[next_building] = max(dp[next_building], dp[building_now] + times[next_building]) # 이전 단계가 전부 완료되어야 다음 단계로 갈 수 있기 때문에 최대값으로 구함
            if degree[next_building] == 0: # 진입 가능한 경우
                q.append(next_building)

    print(dp[W])