# 풍선 터뜨리기 https://www.acmicpc.net/problem/2346

import sys
input = sys.stdin.readline
from _collections import deque

N = int(input())
number = list(map(int, input().split()))    # 종이 리스트
d = deque()
for i in range(N):
    d.append((number[i], i+1))  # (숫자, 인덱스) 형태로 원소 삽입
result = []

current, index = d.popleft()
result.append(index)

for i in range(N-1):
    if current > 0:
        for _ in range(current-1):
            d.append(d.popleft())
    else:
        for _ in range(-current):
            d.appendleft(d.pop())
    current, index = d.popleft()
    result.append(index)

for i in result:
    print(i, end=" ")

# deque에 (숫자, 인덱스) 형태로 넣어주는 것이 문제의 핵심인 것 같다.
