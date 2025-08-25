import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start_point = 0
acc_sum = 0
min_length = N + 1 

for end_point in range(N):
    acc_sum += arr[end_point]  # 구간 합에 현재 원소 더하기

    while acc_sum >= S:  # 부분합이 S 이상일 때
        current_length = end_point - start_point + 1  # 현재 구간 길이
        
        if min_length > current_length: # 현재 길이가 최소길이보다 작은 경우
            min_length = current_length # 갱신
            
        acc_sum -= arr[start_point]  # 시작점 값을 빼서 구간 수축 (더 짧은지 추가 확인용)
        start_point += 1  # 시작점 이동

if min_length == N + 1: # 조건 만족하는 구간이 없을 경우
    print(0)  
else:
    print(min_length)