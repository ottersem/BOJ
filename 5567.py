import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

friends = [[0,[]] for _ in range(n+1)]
visited = [False] * (n+1)
visited[1] = True

for _ in range(m):
    a, b = map(int, input().split())
    friends[a][1].append(b)
    friends[b][1].append(a)

q = deque([1])
cnt = 0
while q:
    depth, f = friends[q.popleft()]
    if depth in (1,2):
        cnt += 1

    for h in f:
        if visited[h] == False:
            visited[h] = True
            q.append(h)
            friends[h][0] = depth + 1

print(cnt)