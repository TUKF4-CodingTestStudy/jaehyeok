# 문제집 https://www.acmicpc.net/problem/1766

import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
solution = [(i for i in range(1, n+1))]
heap = []

for _ in range(m):
    x, y = map(int, input().split())
    heapq.heappush(heap, (y, x))


