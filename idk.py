n = int(input())
friends = []

friends = [list(map(int, input().split())) for _ in range(n)]

limitation = 100000
reachable = []

for x, s in friends:
    pos = set()
    for k in range(limitation // s+1):
        pos.add(x+s*k)
    reachable.append(pos)

common = set.intersection(*reachable)

if common:
    print(min(common))
else:
    print(-1)