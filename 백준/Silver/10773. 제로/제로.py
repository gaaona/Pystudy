import sys

stack = []

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
        
ans = 0

for i in range(len(stack)):
    ans += stack[i]
    
print(ans)