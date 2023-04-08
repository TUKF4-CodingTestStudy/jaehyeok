# 수 정렬하기 https://www.acmicpc.net/problem/2750

import sys
input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    result.append(int(input()))
result.sort()
for i in result:
    print(i)
