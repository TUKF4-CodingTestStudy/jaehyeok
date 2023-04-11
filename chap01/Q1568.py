# 새 https://www.acmicpc.net/problem/1568

n = int(input())
number = 1
time = 0

while n != 0:
    if n < number:
        number = 1
    n -= number
    time += 1
    number += 1

print(time)

