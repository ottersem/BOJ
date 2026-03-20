import sys
input = sys.stdin.readline

n,m = map(int,input().split())
table = [list(map(int,input().split())) for _ in range(n)]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(table[x1-1][y1-1])
    elif x1 == x2 and y1 != y2:
        print(table[x1-1][y1-1:y2])
    else:
        