N, K = map(int, input().split())

ranks = []
for _ in range(N):
    num, gold, silver, bronze = map(int, input().split())
    ranks.append([num, gold, silver, bronze])

ranks.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

cnt = 0
for i in range(N):
    rank = ranks[i]
    if rank[0] == K:
        print(cnt)
        break
    else:
        if i > 0 and rank[1:] == ranks[i-1][1:]:
            continue
        else:
            cnt += 1
    # print(i, cnt)
