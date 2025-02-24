import sys
import heapq

input = sys.stdin.readline
q = []

for i in range(int(input())):
    n = int(input())
    if n == 0:
        if not q:
            print(0)
            continue
        else:
            this = heapq.heappop(q)
            print(this[1])
    else:
        heapq.heappush(q, (abs(n), n))

