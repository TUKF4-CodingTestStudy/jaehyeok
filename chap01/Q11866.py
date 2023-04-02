# 요세푸스 문제0 https://www.acmicpc.net/problem/11866

from _collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
d = deque([i for i in range(1, N + 1)])
result = []

for i in range(1, N + 1):
    for _ in range(K - 1):
        d.append(d.popleft())
    result.append(d.popleft())

print('<', end='')
for i in range(len(result)):
    if i < len(result) - 1:
        print(result[i], end=', ')
    else:  # 마지막 원소
        print(result[i], end='>')
