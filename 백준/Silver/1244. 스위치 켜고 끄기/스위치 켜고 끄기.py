N = int(input())
switches = [-1] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
    gender, num = map(int, input().split())

    i = 1
    if gender == 1:
        while i*num <N+1:
            switches[i*num] = 1 - switches[i*num]
            i += 1
    else:
        left = num
        right = num
        while 0 <= left and right < N+1:
            if switches[left] == switches[right]:
                switches[left] = 1 - switches[left]
                switches[right] = switches[left]
            else:
                break
            left -= i
            right += i

j = 1
if N >= 20:
    while j<N:
        print(*switches[j:j+20])
        j += 20

print(*switches[j:])