# SHA-256 https://www.acmicpc.net/problem/10930
import hashlib

S = input()

result = hashlib.sha256(S.encode())
print(result.hexdigest())
