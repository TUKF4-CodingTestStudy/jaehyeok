# 트럭 https://www.acmicpc.net/problem/13335

import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
bridge = [0] * w
time = 0

while bridge:
    time += 1
    bridge.pop(0)
    if truck:
        if sum(bridge) + truck[0] <= L:
            bridge.append(truck.pop(0))
        else:
            bridge.append(0)
print(time)

# 다리 위에 올라와 있는 트럭과 들어올 트럭의 무게의 합이 L이하일 경우 다리에 올라간다.
# 만약 무게 합이 L보다 클 경우에는 0을 추가해준다.
# 이 문제는 트럭이 못 올라올 경우 0을 넣어주는 것이 키 포인트인 것 같다.
