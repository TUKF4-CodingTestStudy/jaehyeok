# K 번째 수 https://www.acmicpc.net/problem/11004

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
result = list(map(int, input().split()))
result.sort()
print(result[k-1])

