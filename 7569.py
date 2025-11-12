from collections import deque
import sys
input = sys.stdin.readline

m,n,h = map(int, input().split())

nx = [1,-1,0,0,0,0]
ny = [0,0,1,-1,0,0]
nz = [0,0,0,0,1,-1]

boxes = []
for _ in range(h):
    box = [list(map(int,input().split())) for _ in range(n)]
    boxes.append(box)

q = deque()
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

for k in range(h):
    for i in range(n):
        for j in range(m):
            if boxes[k][i][j] == 1:
                q.append([i, j, k, 0])
                visited[k][i][j] = True
            elif boxes[k][i][j] == -1:
                visited[k][i][j] = True

max_days = 0

while q:
    x, y, z, day = q.popleft()
    max_days = max(max_days, day)
    
    for i in range(6):
        dx, dy, dz = x+nx[i], y+ny[i], z+nz[i]
        if 0 <= dx < n and 0 <= dy < m and 0 <= dz < h:
            if not visited[dz][dx][dy] and boxes[dz][dx][dy] == 0:
                visited[dz][dx][dy] = True
                boxes[dz][dx][dy] = 1
                q.append([dx, dy, dz, day + 1])

for i in range(h):
    for j in range(n):
        if 0 in boxes[i][j]:
            print(-1)
            exit()

print(max_days)
