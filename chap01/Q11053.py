# 가장 긴 증가하는 부분 수열 https://www.acmicpc.net/problem/11053

n = int(input())
array = list(map(int, input().split()))
dp = [1] * n    # 초기 배열은 모두 길이가 1이므로 1로 초기화

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:  # 처음부터 i번째까지 값을 비교한다.
            dp[i] = max(dp[i], dp[j] + 1)   # i번째의 길이와 j번째에서 +1 한 값 중에 더 큰 값을 저장한다.
print(max(dp))
