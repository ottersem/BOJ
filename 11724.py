from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())

#Generate nodes
nodes= [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

#Generate Graph
for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

#BFS
def BFS(nodes, idx):
    q = deque(nodes[idx])
    visited = []

    while q:
        curr = q.popleft()
        if curr in visited:
            continue
        q.extend(nodes[curr])
        visited.append(curr)

    return 1, visited

cnt = -1

for idx, node in enumerate(nodes):
    if visited[idx] == True:
        continue
    
    c, visit = BFS(nodes, idx)

    cnt += c
    for i in visit:
        visited[i] = True

print(cnt)