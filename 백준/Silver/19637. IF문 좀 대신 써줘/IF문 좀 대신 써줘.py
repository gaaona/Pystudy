import sys

def binary_search(target,N):
    left, right = 0, N-1
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if target <= nums[mid]:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

N, M = map(int, sys.stdin.readline().split())
nicknames = []

for _ in range(N):
    nickname, num = sys.stdin.readline().split()
    num = int(num)
    nicknames.append((nickname, num))

nicknames.sort(key=lambda x: x[1])

nums = [x[1] for x in nicknames]

for _ in range(M):
    rate = int(sys.stdin.readline().rstrip())
    idx = binary_search(rate,N)
    print(nicknames[idx][0])
