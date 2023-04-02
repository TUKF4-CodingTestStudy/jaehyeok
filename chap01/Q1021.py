# 회전 하는 큐 https://www.acmicpc.net/problem/1021

import sys
from _collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
d = deque([i for i in range(1, N+1)])
data = list(map(int, input().split()))
count = 0

for target in data:
    index = d.index(target)
    if index <= len(d) // 2:
        for _ in range(index):
            d.append(d.popleft())
            count += 1
    else:
        for _ in range(len(d) - index):
            d.appendleft(d.pop())
            count += 1
    d.popleft()
print(count)
