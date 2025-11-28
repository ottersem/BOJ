from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

dy = [2, 2, 1, -1, -2, -2, 1, -1]
dx = [1, -1, 2, 2, 1, -1, -2, -2]

def bfs(size, start, target, board):
    sy, sx = start
    ty, tx = target
    
    if start == target:
        return 0
    
    q = deque()
    q.append((sy, sx, 0))
    board[sy][sx] = True
    
    while q:
        y, x, move = q.popleft()
        if y == ty and x == tx:
            return move
        
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < size and 0 <= nx < size:
                if not board[ny][nx]:
                    board[ny][nx] = True
                    q.append((ny, nx, move+1))

for _ in range(n):
    size = int(input())
    start = tuple(map(int, input().split()))
    target = tuple(map(int, input().split()))
    board = [[False] * size for _ in range(size)]
    print(bfs(size, start, target, board))