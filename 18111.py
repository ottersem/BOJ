from sys import stdin
input = stdin.readline

n,m,b = map(int, input().split())

time = 0
answer = -1

height = [list(map(int, input().split())) for _ in range(n)]

def action(target):
    need = 0   
    remove = 0 
    for i in range(n):
        for j in range(m):
            crt = height[i][j]
            if crt > target:
                remove += crt - target
            elif crt < target:
                need += target - crt
    
    if need > remove + b:
        return -1
    
    time = remove * 2 + need
    return time

min_time = float('inf')
best_h = 0

max_h = max(max(row) for row in height)

for h in range(0, max_h + 1):  
    result = action(h)
    if result != -1:
        if result < min_time:
            min_time = result
            best_h = h
        elif result == min_time and h > best_h:
            best_h = h

print(min_time, best_h)