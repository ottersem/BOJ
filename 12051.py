from sys import stdin

input = stdin.readline

def operationQ(arr):
    cnt = 0
    return cnt

t = int(input())
for i in range(t):
    print(f'Case #{i+1}:')
    r, c = map(int, input().split())
    grid = []
    for _ in range(r):
        grid.append(list(input().rstrip()))

    n = int(input())
    for _ in range(n):
        order = input()
        match order[0]:
            case 'Q':
                pass
            case 'M':
                x, y, z = order[1], order[2], order[3]
                grid[x][y] = z