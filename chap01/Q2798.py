# 블랙잭 https://www.acmicpc.net/problem/2798

N, M = list(map(int, input().split(' ')))
n_list = list(map(int, input().split(' ')))

maximum_value = 0
length = len(n_list)

for i in range(0, length-2):
    for j in range(i+1, length-1):
        for k in range(j+1, length):
            temp = n_list[i]+n_list[j]+n_list[k]
            if maximum_value < temp <= M:
                maximum_value = temp

print(maximum_value)
