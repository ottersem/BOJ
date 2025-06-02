#BFS

from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())

visited = [False for _ in range(100001)]

q = deque()
q.append((n,0))
visited[n] = True

while q:
    curr, time = q.popleft()
    actions = (curr-1, curr+1, curr*2)

    if curr == k:
        print(time)
        break

    for action in actions:
        if 0 <= action < 100001 and not visited[action]:
            visited[action] = True
            q.append((action, time+1))