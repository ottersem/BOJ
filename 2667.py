from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(start_y, start_x):
    q = deque([(start_y, start_x)])
    visited[start_y][start_x] = True
    count = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == False and map[ny][nx] == 1:
                    q.append([ny,nx])
                    visited[ny][nx] = True
                    count += 1
    
    return count

for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and not visited[i][j]:
            answer.append(bfs(i,j))

print(len(answer))
answer.sort()
for size in answer:
    print(size)