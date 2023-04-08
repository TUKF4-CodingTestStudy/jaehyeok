# 나이순 정렬 https://www.acmicpc.net/problem/10814

n = int(input())

array = []

for _ in range(n):
    data = input().split(' ')
    array.append((int(data[0]), data[1]))

# key 속성을 이용해서 (나이, 이름)에서 첫번째 값을 기준으로 정렬하게 하고
# 같을 경우 인덱스가 더 빠른것이 앞으로 오게 된다.
array = sorted(array, key=lambda x: x[0])

for i in array:
    print(i[0], i[1])


# <my 방식> 근데 내 방식이 더빨라 이게 맞나...?
# import sys
# input = sys.stdin.readline
# import heapq
#
# n = int(input())
# member = []
# index = [0] * n
#
# for i in range(n):
#     age, name = input().split()
#     heapq.heappush(member, (int(age), i))
#     index[i] = name
#
# while member:
#     age, i = heapq.heappop(member)
#     print(age, index[i])
