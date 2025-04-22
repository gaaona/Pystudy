def f(n):
    global p

    if p[n] == 0:
        p[n] = f(n-1) + f(n-2)
    
    return p[n]

N = int(input())

p = [0] * (N+1)
p[1] = 1

if N >1:
    p[2] = 2

f(N)
print(p[N]%10007)