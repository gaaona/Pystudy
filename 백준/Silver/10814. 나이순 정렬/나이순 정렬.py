N = int(input())
infos = [0] * N

for i in range(N):
    age, name = input().split()
    infos[i] = (int(age), name)


infos.sort(key=lambda x:x[0]) # 그냥 sort하면 infos[1]도 사전순으로 정렬되는 것 같은데 이렇게 하면 key 기준 외에는 입력 순서대로 됨

for info in infos:
    print(*info)