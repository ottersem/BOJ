import sys
from collections import deque

input = sys.stdin.readline

n,l,r = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1,-1,0,0], [0,0,1,-1]

def border_check(x,y):
    q = deque([(x,y)])
    u = set()
    v[x][y]=1