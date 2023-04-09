# Z https://www.acmicpc.net/problem/1074

N, r, c = map(int, input().split())


def sol(N, r, c):
    if N == 0:
        return 0
    return 2 * (r % 2) + (c % 2) + 4 * sol(N - 1, int(r / 2), int(c / 2))


print(sol(N, r, c))

# 제일 작은 2*2 박스
# 0 1
# 2 3
# 로부터 각각 (0제외)
#
# 좌표 r,c가 2배가 됨에 따라
# 값이 4의 배수로 확장된다.
# ex) 8 (2,0) -> 32 (4,0)
# ex) 14 (2,3) -> 56 (4,6)

# 2*(r%2)+(c%2)는 네모칸 안에서 이동
# 4*sol( N-1, int(r/2), int(c/2))는 4의 배수하기 이전의 값
#
# 예시로
# 44는 11에서 4를 곱한 수 입니다.
# 11은 8에서 3을 더한 값 입니다. ( 2 * (1) + 1 = 3 )
# 8은 2에 4를 곱한 수이고,
# 그래서  0 + 4 * ( 3 + 4 * ( 2 + 4 * ( 0 ) ) ) 는 44 가 나오는 모습.





# 이 방식은 0.5초로 바뀌어서 실패함
# def solve(n, x, y):
#     global result
#     if n == 2:
#         if x == X and y == Y:
#             print(result)
#             return
#         result += 1
#         if x == X and y + 1 == Y:
#             print(result)
#             return
#         result += 1
#         if x + 1 == X and y == Y:
#             print(result)
#             return
#         result += 1
#         if x + 1 == X and y + 1 == Y:
#             print(result)
#             return
#         result += 1
#         return
#     solve(n / 2, x, y)
#     solve(n / 2, x, y + n / 2)
#     solve(n / 2, x + n / 2, y)
#     solve(n / 2, x + n / 2, y + n / 2)
#
#
# N, X, Y = map(int, input().split(' '))
# result = 0
# solve(2 ** N, 0, 0)
