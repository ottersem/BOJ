from sys import stdin
from collections import deque
input = stdin.readline

def BFS(maps, nx, ny, x, y):
    if maps[y][x][0] == 0 or maps[y][x][1] == True:
        return 0

    q = deque([(x,y)])
    maps[y][x][1] == True
    dx = [1,1,1,-1,-1,-1,0,0]
    dy = [1,0,-1,1,0,-1,1,-1]

    while q:
        cx, cy = q.popleft()
        for i in range(8):
            ddx = cx + dx[i]
            ddy = cy + dy[i]
            if 0 <= ddx < nx and 0 <= ddy < ny and maps[ddy][ddx][0] == 1 and not maps[ddy][ddx][1]:
                maps[ddy][ddx][1] = True
                q.append([ddx,ddy])
    return 1

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    maps = [[[0, False] for _ in range(w)] for _ in range(h)]

    for y in range(h):
        xx = list(input().split())
        for x in range(w):
            maps[y][x][0] = int(xx[x])

    cnt = 0

    for y in range(h):
        for x in range(w):
            cnt += BFS(maps=maps, nx=w, ny=h, x=x, y=y)

    print(cnt)