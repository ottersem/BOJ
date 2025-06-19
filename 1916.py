#Dijkstra
from sys import stdin
import heapq

n = int(input())

cities = [[] for _ in range(n+1)]
dist = [float('inf')] * (n+1)

for _ in range(int(input())):
    a, b, time = map(int,input().split())
    cities[a].append((time, b))
    cities[b].append((time, a))

start, end = map(int,input().split())

dist[start] = 0
heap = [(0, start)]

while he