# 절댓값 힙 https://www.acmicpc.net/problem/11286

import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []

for i in range(n):
    data = int(input())
    if data != 0:
        heapq.heappush(heap, (abs(data), data))
    else:
        if heap:
            absolute, original = heapq.heappop(heap)
            print(original)
        else:
            print(0)

# 우선순위 큐를 이용하여 간단히 풀 수 있다.
# 우선 순위 큐에 넣을때 ((절댓값)data, data) 형태의 튜플로 넣어 주는 것이 이 문제의 키포인트이다.
