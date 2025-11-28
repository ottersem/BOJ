import sys
input = sys.stdin.readline

n, h = map(int, input().split())

cards = list(map(int, input().split()))

if sum(cards) < h:
    print(-1)
else:
    for i, d in enumerate(cards):
        h -= d
        if h <= 0:
            print(i)
            exit()
