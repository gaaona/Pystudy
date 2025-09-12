import sys
input = sys.stdin.readline

def find_set(x):
    while parents[x] != x: # 최상단 노드가 아닌 경우
        x = parents[x] # 부모로 설정(한 칸 위로)
    return x


def union(x, y):
    global parents
    
    parents[find_set(y)] = find_set(x) # y의 부모를 x의 부모로 재할당


n, m = map(int, input().split())

parents = [i for i in range(n)]

# 초기 설정
a, b = map(int, input().split())

parents[a] = a 
parents[b] = a

for i in range(2, m+1): # 번째라서 m+1로 생각
    dot_a, dot_b = map(int, input().split())

    if find_set(dot_a) == find_set(dot_b): # 두 점의 부모가 같을 때(사이클 완성)
        print(i) # 번째 출력
        exit()
    union(dot_a, dot_b) # 두 점 부모가 다르니 합치기

print(0)