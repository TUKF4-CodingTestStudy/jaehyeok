# 평범한 배낭 https://www.acmicpc.net/problem/12865

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    weight, value = map(int, input().split())
    for j in range(1, k + 1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])


# 이 문제는 테이블을 그려가면서 이해해야 하는데 테이블의 행은 무게이고 열은 물건의 개수이다.
# 각 요소의 값은 가치이다.
