#BFS-like, check 2606-1.py

from sys import stdin
input = stdin.readline

n = int(input())
pair = int(input())

computers = [[] for _ in range(n+1)]
virus = []

for _ in range(pair):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

cur = [1]

while cur:
    infected = cur.pop()
    virus.append(infected)
    if computers[infected]:
        cur.extend(computers[infected])
        computers[infected] = []
    else:
        continue

print(len(set(virus))-1)

