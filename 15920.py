import sys
input = sys.stdin.readline

n = int(input())

condition = False
time = 1
actions = list(map(str, input()))[:n]

if actions.count('W') < 2:
    print(0)
    exit(0)

for action in actions:
    if action == 'W':
        time += 1
    elif time == 1:
        condition = not condition
    elif time == 2:
        print(6)
        exit(0)
    else:
        break

if condition:
    print(1)
else:
    print(5)