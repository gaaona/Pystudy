import sys

input = sys.stdin.readline

N,M = map(int, input().split())
password_dict = {}

for _ in range(N):
    url, password = input().rstrip().split(" ")
    password_dict[url] = password

for _ in range(M):
    print(password_dict[input().rstrip()])