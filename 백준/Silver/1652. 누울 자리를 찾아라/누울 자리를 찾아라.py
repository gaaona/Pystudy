import sys

def count_available(arr):
    j_cnt = 0

    for i in range(N):
        j = 0
        j_len = 0
        while j < N: # 가로 범위 내에서
            if arr[i][j] == '.': # 빈 공간이면
                j_len += 1 # 누울 자리 길이 세기
            else: # X일 때
                if j_len >= 2: # 누울 수 있으면
                    j_cnt += 1
                j_len = 0 # 누울 자리 길이 초기화
            j += 1 # 다음 j로
        # j==N일 때(행 탐색 끝)
        if j == N and j_len >= 2: # 한 행이 다 빈 공간이거나 벽 다음의 공간이 누울 수 있다면
            j_cnt += 1 # 누울 자리 길이 세기
    return j_cnt

N = int(sys.stdin.readline())

room = [list(sys.stdin.readline()) for _ in range(N)]

j_cnt = count_available(room)
room_reverse = list(map(list,zip(*room))) # 세로로 room 재구성
i_cnt = count_available(room_reverse)

print(j_cnt, i_cnt)