# 오큰수 https://www.acmicpc.net/problem/17298

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = []
NGE = [-1]*N

for i in range(N):
    data = A[i]
    # stack이 비어있거나 내림 차순일 경우 stack에 추가
    if len(stack) == 0 or stack[-1][0] >= data:
        stack.append((data, i))
    else:
        while len(stack) > 0:
            previous, index = stack.pop()
            if previous >= data:
                stack.append((previous, index))
                break
            else:
                NGE[index] = data
        stack.append((data, i))
for i in NGE:
    print(i, end=' ')


