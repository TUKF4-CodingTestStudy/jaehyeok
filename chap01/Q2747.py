# 피보나치 수 https://www.acmicpc.net/problem/2747

n = int(input())

a, b = 0, 1

while n > 0:
    a, b = b, a+b
    n -= 1
print(a)






# 시간초과가 나왔다....
# 이유는 트리 형태여서 한개의 피보나치 수를 구하려고 할 때 그 밑에까지 다 계산 해야하기 때문이다.
# def fibonacci(number):
#     if number == 0:
#         return 0
#     if number == 1:
#         return 1
#     return fibonacci(number - 2) + fibonacci(number - 1)
#
#
# print(fibonacci(n))

