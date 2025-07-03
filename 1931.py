from collections import deque
import sys
input = sys.stdin.readline

conf = list()

for _ in range(int(input())):
    s, e = map(int,input().split())
    conf.append((s,e))

conf.sort(key = lambda x: (x[1], x[0]))
conf = deque(conf)

start, end = conf.popleft()
cnt = 1

for time in conf:
    sn, se = time
    if sn >= end:
        cnt += 1
        start = sn
        end = se

print(cnt)