import sys

N = int(sys.stdin.readline())

liquids = list(map(int, sys.stdin.readline().split()))

cnt = 2000000001
i = 0
j = N-1
ans = (0,0)

while i< j:
    current_sum = liquids[i] + liquids[j]

    if abs(cnt) > abs(current_sum):
        cnt = current_sum
        ans = (liquids[i], liquids[j])

    if current_sum == 0:
        break
    elif current_sum < 0:
        i += 1
    else:
        j -= 1
print(*ans)