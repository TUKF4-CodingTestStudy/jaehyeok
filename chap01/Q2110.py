# 공유기 설치 https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline

n, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = 1
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start + end)//2  # mid는 Gap을 의미한다.
    value = array[0]
    count = 1   # 공유기 갯수
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]    # 공유기 설치
            count += 1
    if count >= c:  # 공유기 갯수가 충분할 경우
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)

# 이진탐색은 start를 늘리고, end를 줄여가며 원하는 값을 찾아간다.

