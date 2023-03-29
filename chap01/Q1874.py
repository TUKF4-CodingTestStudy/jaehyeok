# 스택 수열 https://www.acmicpc.net/problem/1874

n = int(input())

stack = []
result = []
number = 1

for i in range(1, n+1):
    data = int(input())
    while data >= number:
        stack.append(number)
        result.append('+')
        number += 1
    if data == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
print('\n'.join(result))
