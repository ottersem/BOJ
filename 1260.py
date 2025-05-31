from collections import deque
from sys import stdin

input = stdin.readline

n, m, v = map(int, input().split())

nodes = [[[], False] for _ in range (n+1)]

#graph making
for _ in range(m):
    a, b = map(int, input().split())
    nodes[a][0].append(b)
    nodes[b][0].append(a)

#혹시 몰라 정렬
for i in range(1, n+1):
    nodes[i][0].sort()


#DFS
DFS = []
stack = list()
stack.append(v)

while stack:
    curr = stack.pop()
    if nodes[curr][1]:
        continue
    else:
        nodes[curr][1] = True
        DFS.append(str(curr))
        waiting = nodes[curr][0][:]
        while waiting:
            stack.append(waiting.pop())

print(' '.join(DFS))


#그래프 초기화
for i in range(len(nodes)):
    nodes[i][1] = False

#BFS
BFS = []
q = deque()
q.append(v)

while q:
    curr = q.popleft()
    if nodes[curr][1]:
        continue
    else:
        nodes[curr][1] = True
        BFS.append(str(curr))
        q.extend(nodes[curr][0])

print(' '.join(BFS))


