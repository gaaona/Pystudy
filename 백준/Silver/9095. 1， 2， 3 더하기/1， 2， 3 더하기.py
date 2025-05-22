def f(i,cnt):
    global ans

    if cnt == N:
        ans += 1
        return

    if cnt>N:
        return

    for i in range(3):
        if (cnt + nums[i]) <= N:
            f(i, cnt+ nums[i])

T = int(input())

for tc in range(T):
    nums = [3, 2, 1]

    N = int(input())

    ans = 0

    f(0,0)
    print(ans)
