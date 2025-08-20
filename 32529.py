n, m = map(int, input().split())
decay = list(map(int, input().split()))[::-1]

print(decay)

w = 0

for day, weight in enumerate(decay):
    w += weight
    if w >= m:
        print(n-day)
        exit()

print(-1)