import sys
input = sys.stdin.readline

for _ in range(int(input())):
    r, e, c = map(int, input().split())
    if e-c > r:
        print("advertise")
    elif e-c < r:
        print("do not advertise")
    else:
        print("does not matter")