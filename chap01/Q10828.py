# 스택 https://www.acmicpc.net/problem/10828
import sys

input = sys.stdin.readline

test_case = int(input())
stack = []

for _ in range(test_case):
    command = input().strip().split(' ')
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
