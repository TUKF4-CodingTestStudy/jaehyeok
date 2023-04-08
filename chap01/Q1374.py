# 강의실 https://www.acmicpc.net/problem/1374
import heapq
import sys
input = sys.stdin.readline

n = int(input())
lectures = []

for i in range(n):
    id, start, end = map(int, input().split())
    heapq.heappush(lectures, (start, end))

heap = []
end = heapq.heappop(lectures)[1]
heapq.heappush(heap, end)
answer = 1

for i in range(n-1):
    new_start, new_end = heapq.heappop(lectures)
    end = heapq.heappop(heap)

    if new_start < end:     # 가장 빠른 종료 시간 보다 시작 시간이 작으면(겹친다면) 강의실 추가
        heapq.heappush(heap, end)
        heapq.heappush(heap, new_end)
        answer += 1
    else:
        heapq.heappush(heap, new_end)
print(answer)

# 우선순위 큐를 이용하여 시작시간과 종료시간을 비교하는 것이 포인트이다.
