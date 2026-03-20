from sys import stdin
import heapq
input = stdin.readline

V, E = map(int, input().split())
K = int(input())
nodes = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int, input().split()) # u->v, cost = w
    nodes[u].append((w,v))

def dijkstra(start, n, graph):
    INF = int(1e9)
    distance = [INF] * (n+1)

    q=[]
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist : continue

        for i in graph[now]:
            next_node = i[1]
            cost = dist + i[0]

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance
    
distance = dijkstra(K,V, nodes)

for i in distance[1:]:
    if i == int(1e9):
        print("INF")
    else : print(i)
    