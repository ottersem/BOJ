import sys
input = sys.stdin.readline

n, m = map(int, input().split())

grid = [[True] * n for _ in range(n)]


for _ in range(m):
    x, y, k = map(int, input().split())
    x -= 1  
    y -= 1 
    
    match k:
        case 1:
            for i in range(n):
                if i >= x or i != y:
                    grid[i][y] = False
        case 2: 
            for i in range(n):
                for j in range(n):
                    if i >= x or j <= y:
                        grid[i][j] = False
        case 3:
            for j in range(n):
                if j <= y:
                    grid[x][j] = False
            for i in range(n):
                if i != x:
                    for j in range(n):
                        grid[i][j] = False
        case 4:
            for i in range(n):
                for j in range(n):
                    if i <= x or j <= y:
                        grid[i][j] = False
        case 5: 
            for i in range(n):
                if i <= x or i != y:
                    grid[i][y] = False
        case 6:  
            for i in range(n):
                for j in range(n):
                    if i <= x or j >= y:
                        grid[i][j] = False
        case 7:  
            for j in range(n):
                if j >= y:
                    grid[x][j] = False
            for i in range(n):
                if i != x:
                    for j in range(n):
                        grid[i][j] = False
        case 8:  
            for i in range(n):
                for j in range(n):
                    if i >= x or j >= y:
                        grid[i][j] = False

for i in range(n):
    for j in range(n):
        if grid[i][j]:
            print(i + 1, j + 1)
            