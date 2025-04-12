arr = list(input())

stack = []

cnt = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append('(')
    else: # 닫는 괄호인 경우
        stack.pop() # 막대 개수 세기 위해 pop
        if arr[i-1] == ')': # 레이저 아님
            cnt += 1
        else: # 레이저인 경우
            cnt += len(stack)

print(cnt)