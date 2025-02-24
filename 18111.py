import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]

def checking(std, height, n, m):
    minus = []
    plus = []
    zero = []
    for i in range(n):
        for j in range(m):
            num = int(std-height[n][m])
            if num>0:
                plus.append(num)
            elif num==0:
                zero.append(num)
            else:
                minus.append(num)