from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int,input().split())

grid = []
answer = [[-1 for _ in range(m)] for _ in range(n)]
start = None

for y in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for x, val in enumerate(row):
        if val == 2:
            start = (y, x)
        if val == 0:
            answer[y][x] = 0  


dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = [[False] * m for _ in range(n)]
q = deque()
q.append((start[0], start[1]))
visited[start[0]][start[1]] = True
answer[start[0]][start[1]] = 0

while q:
    y, x = q.popleft()

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= ny < n and 0 <= nx < m:
            if not visited[ny][nx] and grid[ny][nx] == 1:
                visited[ny][nx] = True
                answer[ny][nx] = answer[y][x] + 1
                q.append((ny,nx))

for row in answer:
    print(*row)