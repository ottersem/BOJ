import sys
input = sys.stdin.readline

n,m = map(int,input().split())

A = []

for _ in range(n):
    A.append(int(input()))

B = sorted(A)

index_map = {}
for i, val in enumerate(B):
    if val not in index_map:
        index_map[val] = i

for _ in range(m):
    d = int(input())
    print(index_map.get(d, -1))