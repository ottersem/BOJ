from sys import stdin
from collections import deque

input = stdin.readline

dq = deque()

for _ in range(int(input())):
    order = input()
    match order[:2]:
        case 'pu':
            num = order.split()[1]
            dq.append(num)
        case 'po':
            print(dq.popleft() if dq else -1)
        case 'si':
            print(len(dq))
        case 'em':
            print(0 if dq else 1)
        case 'fr':
            print(dq[0] if dq else -1)
        case 'ba':
            print(dq[-1] if dq else -1)