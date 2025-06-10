import sys

P = int(input())

for _ in range(P):
    ans = 0
    students = list(map(int, sys.stdin.readline().split()))
    tc = students[0]

    for i in range(2, 21):
        j = i - 1
        while j >= 1 and students[i] < students[j]:
            ans += 1
            students[i], students[j] = students[j], students[i]
            i = j
            j -= 1
    print(f'{tc} {ans}')