from sys import stdin
input = stdin.readline

dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,0,-1]

while True:
    r,c = map(int,input().split())
    if r == 0 and c == 0:
        break

    grid = [list(input().strip()) for _ in range(r)]

    for y, line in enumerate(grid):
        for x, comp in enumerate(line):
            if grid[y][x] == '.':
                grid[y][x] = 0
                for i in range(8):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if 0 <= nx < c and 0 <= ny < r:
                        if grid[ny][nx] == '*':
                            grid[y][x] += 1

    for line in grid:
        print(''.join(map(str, line)))