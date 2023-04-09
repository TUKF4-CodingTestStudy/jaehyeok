# 0 만들기 https://www.acmicpc.net/problem/7490
import copy


def recursive(array, n):
    if len(array) == n:
        operator_list.append(copy.deepcopy(array))  # array를 그냥 쓰게 되면 같은 배열을 사용하므로 카피를 해서 넣어준다.
        return
    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()


test_case = int(input())

for _ in range(test_case):
    operator_list = []
    N = int(input())
    recursive([], N - 1)    # ex) operator_list = [[' ', ' '], [' ', '+'], [' ', '-'] ... ] 총 3**(N-1)
    number_list = [i for i in range(1, N + 1)]
    for operator in operator_list:
        string = ""
        for i in range(N - 1):
            string += str(number_list[i]) + operator[i]
        string += str(number_list[-1])  # 마지막 숫자를 넣어줌
        if eval(string.replace(" ", "")) == 0:  # ' '는 붙여줘야 하므로 공백을 제거해준다.
            print(string)
    print()


