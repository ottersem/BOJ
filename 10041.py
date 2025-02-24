import sys

input = sys.stdin.readline

w, h, n = map(int, input().split())
x, y = map(int, input().split())
cnt = 0

for _ in range(n-1):
    xx, yy = map(int, input().split())

    if not (1 <= xx <= w and 1 <= yy <= h):
        continue

    dx, dy = xx - x, yy - y

    if dx * dy > 0: 
        cnt += max(abs(dx), abs(dy))
    else: 
        cnt += abs(dx) + abs(dy)
    x, y = xx, yy  

print(cnt)
