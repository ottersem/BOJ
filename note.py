import heapq
from sys import stdin
input = stdin.readline

q = []

n = int(input())
for _ in range(n):
    i = int(input())
    if i == 0:
        if len(q) == 0 : print(0)
        else : print(heapq.heappop(q)[1])
        continue
    
    heapq.heappush(q, (abs(i), i))