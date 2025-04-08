N = int(input())

min_cnt = 5000

for i in range(N//5+1):
    remain = N - 5 * i

    # print(remain, i, remain//3)
    if remain%3 == 0:
        cnt = remain//3 + i

        if min_cnt > cnt:
            min_cnt = cnt

if min_cnt == 5000:
    print(-1)
else:
    print(min_cnt)
