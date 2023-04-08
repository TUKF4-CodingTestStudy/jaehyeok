# 수 정렬하기 3 https://www.acmicpc.net/problem/10989

import sys
input = sys.stdin.readline

n = int(input())
result = [0] * 10001

for _ in range(n):
    data = int(input())
    result[data] += 1

for i in range(len(result)):
    if result[i] != 0:
        for _ in range(result[i]):
            print(i)


# 계수 정렬 알고리즘을 사용해야 함.
# 수의 범위가 작을 때 사용할 수 있다. ex) 1~10000
# 배열의 인덱스를 값으로 본다. ex) [0, 1, 2, 3 ,4]
