N = int(input())
T = int(input())

apt = list(map(int, input().split()))

nums = list(map(int, input().split()))

rear = 0
for i in range(T):
    rear += (nums[i] - 1)
    print(apt[rear%(2*N)], end=' ')