from sys import stdin
from operator import itemgetter
input = stdin.readline

n = int(input())
d = dict()
for _ in range(n):
    crt = int(input())
    if crt in d.keys():
        d[crt] += 1
    else:
        d[crt] = 1


answer = sorted(d.items(), reverse=True, key=itemgetter(1))

biggest = 0
pp = set()
for card in answer:
    if card[1] >= biggest:
        biggest = card[1]
        pp.add(card[0])
    else:
        break

print(min(pp))