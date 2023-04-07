# 알파벳 찾기 https://www.acmicpc.net/problem/10809

s = input()
alphabet = [-1] * 26

for i in range(len(s)):
    index = ord(s[i]) - ord('a')
    if alphabet[index] == -1:
        alphabet[index] = i

for i in alphabet:
    print(i, end=' ')

# ord() 함수를 써 하나의 문자를 유니코드로 만들어 주는 것이 포인트! ex) 'a' = 97
