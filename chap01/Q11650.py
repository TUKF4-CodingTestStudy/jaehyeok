# 좌표 정렬하기 https://www.acmicpc.net/problem/11650

import sys

input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    x, y = map(int, input().split())
    result.append((x, y))

# 파이썬에서 기본 정렬 라이브러리는 튜플의 인덱스 순서대로 정렬한다.
# 즉, (x, y, z)가 있으면 x -> y -> z 순서대로 우선순위를 갖는다.
result.sort()
for i in range(n):
    x = result[i][0]
    y = result[i][1]
    print(x, y)
