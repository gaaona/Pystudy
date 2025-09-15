import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().split()))
nums.sort()

ans = (0, 0, 0)
min_sum = 3000000001

if N == 3:
    print(*nums)
    exit()

for i in range(N-2): # i 고정하여 탐색 i,j,k가 N-3,N-2,N-1이 최대니까 range(N-2)
    if i > 0 and nums[i] == nums[i-1]: # 중복된 수 건너뛰기
        continue
    j = i+1
    k = N-1

    while j<k: # 0<=i<j<k<N
        current_sum = nums[i] + nums[j] + nums[k]
        
        if current_sum == 0:
            print(nums[i] , nums[j] , nums[k])
            exit()
            
        if min_sum > abs(current_sum): # 지금 최소합보다 더 작은 경우
            ans = (nums[i] , nums[j] , nums[k])
            min_sum = abs(current_sum)
            
        if current_sum > 0:
            k -= 1
        else:
            j += 1

print(*ans)