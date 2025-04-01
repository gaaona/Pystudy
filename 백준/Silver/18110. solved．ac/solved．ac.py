import sys

def real_roundup(num):
    num_int = int(num)
    diff = num - num_int
    
    if diff >= 0.5:  # 파이썬의 경우 소수점이 0.5면 반올림이나 반내림 수 중에 짝수인 수를 반환한다함;; 수제로 반올림해줍니다
        num = num_int + 1
    
    return int(num)

N = int(sys.stdin.readline())
if N == 0:  # 난이도 의견은 1부터인데 의견의 개수는 0개부터인 요상한 문제입니다. 이걸 하지 않으면 오류가 뜹니다
    answer = 0
else:
    scores = [0] * N  # 의견이 있는 경우(N이 1 이상인 경우)

    for i in range(N):
        scores[i] = int(sys.stdin.readline())

    scores.sort()  # 절사평균 하기 위해 정렬

    M = N * 0.15  # 절사평균 인원 계산용
    M = real_roundup(M)
    
    answer = sum(scores[M:N - M]) / (N - M * 2)  # 절사평균 계산
    
    answer = real_roundup(answer)
    
print(answer)