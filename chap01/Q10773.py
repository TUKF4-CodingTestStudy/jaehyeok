# 제로 https://www.acmicpc.net/problem/10773

import sys

input = sys.stdin.readline

k = int(input())
stack = []

for _ in range(k):
    data = int(input())
    if data != 0:
        stack.append(data)
    else:
        stack.pop()
print(sum(stack))
