from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

moveto = {}
for _ in range(n+m):
    x,y = map(int, input().split())
    moveto[x] = y

visited = [False] * 101
visited[1] = True
distance = [0] * 101

q = deque([(1,0)]) # current position, dice rolled


while q:
    pos, roll = q.popleft()

    if pos == 100:
        print(roll)
        exit()
    
    for dice in range(1,7):
        next_pos = pos+dice
        if next_pos <= 100 and not visited[next_pos]:
            final_pos = moveto.get(next_pos, next_pos)
            visited[final_pos] = True
            distance[final_pos] = roll + 1
            q.append([final_pos, roll+1])