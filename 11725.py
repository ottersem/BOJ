import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)
visited = [False] * (N+1)
visited[1] = True

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])

while queue:
    node = queue.popleft()

    for n in graph[node]:
        if not visited[n]:
            visited[n] = True
            parent[n] = node
            queue.append(n)

print(parent)

for i in range(2,N+1):
    print(parent[i])