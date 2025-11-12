from sys import stdin
from collections import deque
input = stdin.readline

n, m, k, x = map(int, input().split())

cities = [[] for _ in range(n+1)]
distance = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    cities[a].append(b)

queue = deque([x])
distance[x] = 0

while queue:
    city = queue.popleft()
    
    for next_city in cities[city]:
        if distance[next_city] == -1:
            distance[next_city] = distance[city] + 1
            queue.append(next_city)

result = []
for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)

if result:
    result.sort()
    for city in result:
        print(city)
else:
    print(-1)