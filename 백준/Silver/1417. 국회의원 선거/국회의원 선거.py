import heapq

def bribe():
    global dasom, other_votes, ans

    while other_votes:  # 모든 후보자의 표를 매수할 때 까지
        max_vote, candidate = heapq.heappop(other_votes)
        max_vote = -max_vote  # 음수로 넣었으니까 원복

        if dasom < max_vote:  # 최대가 아닌 경우
            diff = max_vote - dasom
            buy = diff % 2 + diff // 2  # 차이의 반 초과 값을 매수해야 최대 값보다 커짐

            dasom += buy  # 다솜 표도 재할당
            ans += buy  # 정답에도 추가
        elif dasom == max_vote:  # 같은 경우(1표만 가져오면 됨)
            ans += 1
            dasom += 1
        else:  # 다솜이 최대인 경우
            break  # 탐색 끝

    return


N = int(input())

dasom = int(input())
ans = 0

if N == 1:  # 단일 후보인 경우 (없으면 매수 안 해도 됨)
    pass
else:
    other_votes = []  # 우선순위 큐

    for _ in range(N-1):
        heapq.heappush(other_votes, -int(input()))

    while other_votes:  # 모든 후보자의 표를 매수할 때 까지
        max_vote = heapq.heappop(other_votes)
        max_vote = -max_vote  # 음수로 넣었으니까 원복

        if dasom > max_vote:  # 최대가 된 경우
            break  # 탐색 끝
        else:  # 다솜이 최대가 아닌 경우 
            max_vote -= 1
            ans += 1
            dasom += 1
            heapq.heappush(other_votes, -max_vote)

print(ans)