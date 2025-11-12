import sys
input = sys.stdin.readline

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]
blue = 0 # 1
white = 0 # 0

def solve(x,y,size):
    global blue,white

    count = 0
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] == 1:
                count += 1

    if count in (0, size * size):
        if count == 0:
            white += 1
        else:
            blue += 1
    else:
        solve(x,y, size//2)
        solve(x, y+size//2, size//2)
        solve(x+size//2,y, size//2)
        solve(x+size//2,y+size//2, size//2)


solve(0,0,n)

print(white)
print(blue)