# 이중 우선순위 큐 https://www.acmicpc.net/problem/7662

import sys
input = sys.stdin.readline
import heapq

test_case = int(input())


def pop(heap):
    while len(heap) > 0:
        data, id = heapq.heappop(heap)
        if not deleted[id]: # 이 과정을 이용해서 최대힙과 최소힙을 동기화 해준다
            deleted[id] = True
            return data
    return None


for i in range(test_case):
    k = int(input())
    max_heap = []
    min_heap = []
    deleted = [False] * (k + 1)
    current = 0
    for j in range(k):
        calculator, value = input().split()
        value = int(value)
        if calculator == "I":
            # 입력 값이 양수면 최대 힙에 저장 단, 작을수록 우선순위가 높으므로 -로 저장
            heapq.heappush(max_heap, (-value, current))
            # 입력 값이 음수면 최소 힙에 저장
            heapq.heappush(min_heap, (value, current))
            current += 1
        else:
            if value == 1:
                pop(max_heap)
            else:
                pop(min_heap)
    max_value = pop(max_heap)
    if max_value is None:
        print("EMPTY")
    else:
        heapq.heappush(min_heap, (-max_value, current))
        print(-max_value, pop(min_heap))

# deleted = [False] * (k + 1)를 이용해서 삭제된 노드를 확인하는 것이 포인트이다.
