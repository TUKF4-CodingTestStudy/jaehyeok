# 트로피 진열 https://www.acmicpc.net/problem/1668

n = int(input())
trophy = [int(input()) for _ in range(n)]
max_height = 0
left = 0
right = 0

for i in range(n):
    if max_height < trophy[i]:
        left += 1
        max_height = trophy[i]

max_height = 0
for i in range(n-1, -1, -1):    # n-1부터 0까지 -1
    if max_height < trophy[i]:
        right += 1
        max_height = trophy[i]

print(left)
print(right)

