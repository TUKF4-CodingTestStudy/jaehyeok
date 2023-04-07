# 연결 요소의 개수 https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n+1)    # 1부터 시작 하는거 주의!
for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    x, y = map(int, input().split())
    union_parent(parent, x, y)

count = set()
for i in range(1, n+1):
    count.add(find_parent(parent, i))
print(len(count))

# union_find를 이용하고, 마지막에 집합으로 카운트 하는 것이 포인트다
