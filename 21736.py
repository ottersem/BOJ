# Graph, BFS

from sys import stdin
from collections import deque

input = stdin.readline

y, x = map(int, input().split())

maps = []
visited = [[False for _ in range(x)] for _ in range(y)]

start = None
           
for ny in range(y):
    row = list(input().strip())
    maps.append(row)

    if 'I' in row:
        start = (row.index('I'), ny)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
q.append(start)
visited[start[1]][start[0]] == True

cnt = 0

while q:
    nx, ny = q.popleft()

    if maps[ny][nx] == 'P':
        cnt += 1

    for i in range(4):
        ddx = nx + dx[i]
        ddy = ny + dy[i]

        if 0 <= ddx < x and 0 <= ddy < y:
            if not visited[ddy][ddx] and (maps[ddy][ddx] == 'O' or maps[ddy][ddx] == 'P'):
                visited[ddy][ddx] = True
                q.append((ddx, ddy))

print('TT' if cnt == 0 else cnt)