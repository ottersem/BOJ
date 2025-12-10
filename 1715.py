import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
answer = 0

for _ in range(n) : 
    heapq.heappush(q, int(input()))

while q:
    if len(q) == 1:
        print(answer)
        break
    a, b = heapq.heappop(q), heapq.heappop(q)
    answer += a+b
    heapq.heappush(q, a+b)


