from sys import stdin
from collections import deque
input = stdin.readline

n,m = map(int,input().split())

grid = [list(map(str, input().strip())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0,0,1))
visited[0][0] = True

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while q:
    x, y, cnt = q.popleft()
    if x == m-1 and y == n-1:
        print(cnt)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if grid[ny][nx] == '1' and not visited[ny][nx]:
                q.append((nx, ny, cnt+1))
                visited[ny][nx] = True