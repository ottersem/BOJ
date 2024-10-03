import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

pc = [False] * n
pc[0] = True
for _ in range(m):
    a, b = map(int, input().split())
    if pc[a-1]:
        pc[b-1] = True
    
print(pc.count(True)-1)
