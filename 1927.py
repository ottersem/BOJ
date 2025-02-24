import sys
from queue import PriorityQueue
input = sys.stdin.readline

q = PriorityQueue()

for _ in range(int(input())):
    i = int(input())
    if i == 0:
        if q.empty():
            print(0)
            continue
        else:
            print(q.get())
    else:
        q.put(i)
