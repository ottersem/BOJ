import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
answer = 1
area = [list(map(int, input().split())) for _ in range(n)]

flood_min = min(map(min,area))
flood_max = max(map(max,area))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(sy,sx,f,visited):
    q = deque()
    q.append((sy,sx))
    visited[sy][sx] = True
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and area[ny][nx] > f:
                    visited[ny][nx] = True
                    q.append((ny, nx))

for f in range(flood_min, flood_max+1):
    visited = [[False]*n for _ in range(n)]
    safe_zone = 0
    for y in range(n):
        for x in range(n):
            if area[y][x] > f and not visited[y][x]:
                safe_zone += 1
                bfs(y,x,f,visited)
    answer = max(answer, safe_zone)

print(answer)