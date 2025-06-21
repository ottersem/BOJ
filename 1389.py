from collections import deque
from sys import stdin
input = stdin.readline

n,m = map(int,input().split())

connections = [[] for _ in range(n+1)]
kevin = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    connections[a].append(b)
    connections[b].append(a)

for i in range(1, n+1):
    q = deque()
    visited = [None] *(n+1)
    q.append(i)
    visited[i] = 0
    
    while q:
        crt = q.popleft()
        for connection in connections[crt]:
            if not visited[connection]:
                visited[connection] = visited[crt] + 1
                q.append(connection)

    kevin[i] = sum(visited[1:])

minimum = min(kevin[1:])
print(kevin.index(minimum))