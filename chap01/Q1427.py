# 소트인사이드 https://www.acmicpc.net/problem/1427

n = input()

for i in range(10):
    for j in n:
        if ord(j) == (ord('9') - i):
            print(j, end='')

