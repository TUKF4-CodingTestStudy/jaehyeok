# 사이클 게임 https://www.acmicpc.net/problem/20040

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
parent = [0] * n
for i in range(n):
    parent[i] = i
cycle = False

for i in range(m):
    x, y = map(int, input().split())
    if find_parent(parent, x) == find_parent(parent, y):
        cycle = True
        print(i+1)
        break
    else:
        union_parent(parent, x, y)
if not cycle:
    print(0)

# union_find만 익히면 무난하게 할 수 있는 문제다.
