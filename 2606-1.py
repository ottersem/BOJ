from collections import deque
from sys import stdin

input = stdin.readline

n = int(input())
computers = [[] for _ in range(n+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

visited = [False] * (n+1)

q = deque([1])
visited[1] = True
count = 0

while q:
    cur = q.popleft()

    for neighbor in computers[cur]:
        if not visited[neighbor]:
            visited[neighbor] = True
            q.append(neighbor)
            count += 1


print(count)