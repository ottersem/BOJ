from sys import stdin
from collections import deque

input = stdin.readline

m, n = map(int,input().split())

grid = []
q = deque()
visited = [[[False, 0] for _ in range(m)]for _ in range(n)] ##[[is_visited, time]]


for y in range(n):
    row = list(map(int,input().split()))
    grid.append(row)

    for x, val in enumerate(row):
        if val == 1:
            q.append((y,x))
            visited[y][x][0] = True
            visited[y][x][1] = 1
        elif val == -1:
            visited[y][x][0] = True
            visited[y][x][1] = -1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while q:
    y, x = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < n and 0 <= nx < m:
            if not visited[ny][nx][0] and grid[ny][nx] != -1:
                visited[ny][nx][0] = True
                visited[ny][nx][1] = visited[y][x][1] + 1
                q.append((ny,nx))

# print('\n'.join(' '.join(f"{v[0]}:{v[1]}" for v in row) for row in visited))

if 0 in list(v[1] for row in visited for v in row):
    print(-1)
else:
    print(visited[y][x][1] - 1)