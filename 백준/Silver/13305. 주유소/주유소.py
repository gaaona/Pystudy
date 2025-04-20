N = int(input())

edges = list(map(int,input().split()))

oil_prices = list(map(int,input().split()))

ei = pi = 0
total = 0

while pi<N-1:
    if ei == N-1:
        break

    if oil_prices[pi] > oil_prices[pi+1] or ei == N-2:
        total += (oil_prices[pi] * edges[ei])
        pi += 1
    else:
        edges[ei+1] += edges[ei]
        
    ei += 1

print(total)