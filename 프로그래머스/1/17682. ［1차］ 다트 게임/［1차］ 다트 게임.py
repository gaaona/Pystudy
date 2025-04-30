def solution(dartResult):
    answer = 0

    N = len(dartResult)
    res = [0] * 4
    di = ri =0

    while di<N:
        x = dartResult[di]
        if x.isdecimal():
            ri += 1
            if di+1<N and x == '1' and dartResult[di+1] == '0':
                res[ri] = 10
                di += 1
            else:
                res[ri] = int(x)
            di += 1
            continue

        if dartResult[di] == 'D':
            res[ri] = res[ri] ** 2
        elif dartResult[di] == 'T':
            res[ri] = res[ri] ** 3
        elif dartResult[di] == '*':
            res[ri-1] *= 2
            res[ri] *= 2
        elif dartResult[di] == '#':
            res[ri] *= (-1)
        di += 1
        continue
    answer = sum(res)

    return answer
