T = int(input())

for _ in range(T):
    N = int(input())
    triangle = [0] * (N+1)

    triangle[1] = 1
    
    if N>=2: # N은 1부터라서
        triangle[2] = 1

    if N>=3:
        for i in range(3,N+1):
            triangle[i] = triangle[i-2] + triangle[i-3]
    print(triangle[N])