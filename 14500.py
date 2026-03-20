from sys import stdin
input = stdin.readline

r, c = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False] * c for _ in range(r)]
max_val = 0

def dfs(x, y, cnt, total):
    global max_val
    
    if cnt == 4:
        max_val = max(max_val, total)
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1, total + paper[nx][ny])
            visited[nx][ny] = False

def check_t(x, y):
    t_shapes = [
        [(0,0), (0,1), (0,2), (1,1)],  # ㅜ
        [(0,1), (1,0), (1,1), (1,2)],  # ㅗ
        [(0,0), (1,0), (2,0), (1,1)],  # ㅏ
        [(0,1), (1,1), (2,1), (1,0)]   # ㅓ
    ]
    
    result = 0
    for shape in t_shapes:
        try:
            temp = sum(paper[x + dx][y + dy] for dx, dy in shape)
            result = max(result, temp)
        except IndexError:
            continue
    return result

for i in range(r):
    for j in range(c):
        visited[i][j] = True
        dfs(i, j, 1, paper[i][j])
        visited[i][j] = False
        max_val = max(max_val, check_t(i, j))

print(max_val)