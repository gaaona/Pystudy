import sys

def f(nums, budget):
    left, right = 0, max(nums)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for num in nums:
            total += min(num, mid)
        if total <= budget:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer

# 입력 처리
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())

# 결과 출력
print(f(nums, budget))
