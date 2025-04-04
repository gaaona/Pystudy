people = int(input())

size = list(map(int,input().split()))

T, P = map(int,input().split())

tshirt = 0
for num in size:
    tmp = num//T
    if num% T > 0:
        tmp += 1

    tshirt += tmp

pen = people//P
each_pen = people%P

print(tshirt)
print(pen,each_pen)