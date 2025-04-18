import sys

arr = [0] * 20000001
# 0번: 0, 1~10,000,000번: 1~10,000,000, 10,000,001~20,000,000번:-10,000,000부터 -1.

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
find_list = list(map(int, sys.stdin.readline().split()))

for num in num_list:
    arr[num] += 1

for find in find_list:
    print(arr[find], end=" ")