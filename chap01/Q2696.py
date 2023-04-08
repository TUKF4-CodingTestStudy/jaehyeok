# 중앙값 구하기 https://www.acmicpc.net/problem/2696

import sys

input = sys.stdin.readline
import heapq


def show_result():
    print(len(result))
    for i in range(len(result)):
        print(result[i], end=' ')
        if (i + 1) % 10 == 0:
            print()
    print()


for _ in range(int(input())):
    m = int(input())
    data = []
    for i in range(m // 10 + 1):
        data.extend(list(map(int, input().split())))
    left = []   # 중앙 값보다 작으면 최대 힙(원소 삽입할 경우 음수 부호)
    right = []  # 중앙 값보다 크면 최소 힙
    median = data[0]
    result = [median]
    for i in range(1, m):
        if data[i] <= median:
            heapq.heappush(left, -data[i])
        else:
            heapq.heappush(right, data[i])
        if i % 2 == 0:  # 홀수 번째 마다
            if len(left) > len(right): # 왼쪽 -> 오른쪽으로 이동
                heapq.heappush(right, median)
                median = -heapq.heappop(left)
            elif len(left) < len(right):   # 오른쪽 -> 왼쪽으로 이동
                heapq.heappush(left, -median)
                median = heapq.heappop(right)
            result.append(median)
    show_result()

# 최대힙 - 중앙값 - 최소힙 형식을 생각 하고, 홀수 번째 마다 앙쪽 힙의 갯수를 맞춰주는 것이 포인트이다.
