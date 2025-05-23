from collections import deque

n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))

onboard = deque()
time = 1

while trucks:
    if len(onboard) >= w or sum(onboard) + trucks[0] >= l:
        time += len(onboard) + w -1
        onboard = deque()
    else:
        onboard.append(trucks.popleft())

print(time)