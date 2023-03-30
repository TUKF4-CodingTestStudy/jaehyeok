# 수 찾기 https://www.acmicpc.net/problem/1920

N = int(input())
A = set(map(int, input().split(' ')))
M = int(input())
data = list(map(int, input().split(' ')))

for i in data:
    if i in A:
        print(1)
    else:
        print(0)
