from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
board = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
board_blind = []

for i in range(n):
    row =[]
    for j in range(n):
        if board[i][j] == 'R':
            row.append('G')
        else:
            row.append(board[i][j])
    board_blind.append(row)

normal = 0
blind = 0

nx = [1,-1,0,0]
ny = [0,0,1,-1]

def bfs(x,y,color,target_board):
    global n
    q = deque()
    q.append([y,x])
    visited[y][x] = True

    while q:
        y, x = q.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if 0<=dx<n and 0<=dy<n:
                if target_board[dy][dx] == color:
                    if visited[dy][dx] == False:
                        q.append([dy,dx])
                        visited[dy][dx] = True

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(j,i,board[i][j], board)
            normal += 1

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(j,i,board_blind[i][j], board_blind)
            blind += 1

print(normal, blind)
