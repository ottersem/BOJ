from sys import stdin
from collections import deque

input = stdin.readline

case = int(input())


# def BFS(maps, x, y, m, n):
#     neighbor = []

#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]

#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]

#         if 0 <= xx < m and 0 <= yy < n:
#             continue

#         if maps[yy][xx] == True:
#             neighbor.append([xx, yy])

#     return neighbor

def BFS(maps, sx, sy, m, n):
    q = deque()
    q.append((sx, sy))
    maps[sy][sx] = False

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx]:
                maps[ny][nx] = False
                q.append((nx, ny))


##must add case iteration under this line

for _ in range(case):
    m, n, k = map(int, input().split())
    maps = [[False for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        maps[y][x] = True

    cnt = 0

    for y in range(n):
        for x in range(m):
            if maps[y][x]:
                BFS(maps, x, y, m, n)
                cnt += 1

    print(cnt)