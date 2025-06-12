def find_heart():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '*':
                return i+2, j+1  # 심장 위치(머리 아래)

N = int(input())
matrix = [input().strip() for _ in range(N)]

hx, hy = find_heart()
print(hx, hy)

# 방향: 왼팔(-x), 오른팔(+x), 허리(+y)
arm_left = 0
for j in range(hy-2, -1, -1):
    if matrix[hx-1][j] == '*':
        arm_left += 1

arm_right = 0
for j in range(hy, N):
    if matrix[hx-1][j] == '*':
        arm_right += 1

waist = 0
y = hx
while y < N and matrix[y][hy-1] == '*':
    waist += 1
    y += 1

leg_left = 0
for i in range(y, N):
    if matrix[i][hy-2] == '*':
        leg_left += 1

leg_right = 0
for i in range(y, N):
    if matrix[i][hy] == '*':
        leg_right += 1

print(arm_left, arm_right, waist, leg_left, leg_right)