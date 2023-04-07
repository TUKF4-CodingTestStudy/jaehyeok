# 소수의 곱 https://www.acmicpc.net/problem/2014
import heapq
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
data = list(map(int, input().split()))

heap = []
visited = set()     # 이미 처리된 수
max_value = max(data)

for x in data:
    heapq.heappush(heap, x)

for i in range(n-1):    # 큐에서 N번 빼면 그게 N번째 수이다.
    element = heapq.heappop(heap)
    for x in data:
        now = element * x
        if len(heap) >= n and max_value < now:  # 힙의 크기가 N이상이고, 힙의 최댓값보다 곱한 결과가 더 크면 뺄 일이 없으므로 안넣는다.
            continue
        if now not in visited:
            heapq.heappush(heap, now)
            max_value = max(max_value, now)
            visited.add(now)

print(heapq.heappop(heap))

