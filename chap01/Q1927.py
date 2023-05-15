# 최소 힙 https://www.acmicpc.net/problem/1927

import sys
input = sys.stdin.readline
import heapq

heap = []
n = int(input())

for _ in range(n):
    data = int(input())
    if data == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, data)
