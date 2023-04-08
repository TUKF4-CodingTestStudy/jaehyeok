# 주사위 https://www.acmicpc.net/problem/1233

s1, s2, s3 = map(int, input().split())

total = [0] * (s1 + s2 + s3 + 1)

for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            total[i+j+k] += 1
for i in range(len(total)):
    if total[i] == max(total):
        print(i)    # 배열의 인덱스가 정답이 된다.
        break

# 최대 빈도수가 같으면 더 작은 값을 반환하는 것이 포인트이다.
