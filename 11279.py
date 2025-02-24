import sys
import heapq
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    i = int(input())
    if i == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -i)