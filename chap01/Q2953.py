# 나는 요리사다 https://www.acmicpc.net/problem/2953

import sys
input = sys.stdin.readline

winner, max_score = 0, 0

for i in range(1, 6):
    score = list(map(int, input().split()))
    total_score = sum(score)
    if max_score < total_score:
        max_score = total_score
        winner = i

print(winner, max_score)
