# 수 정렬하기 2 https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline

n = int(input())
list = []

for _ in range(n):
    data = int(input())
    list.append(data)
list.sort()

for i in range(n):
    print(list[i])

