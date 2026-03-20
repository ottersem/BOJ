from math import prod
import sys
input = sys.stdin.readline

n = int(input())
participants = {int(line.split()[0]):list(map(int, line.split()[1:])) for _ in range(n) for line in [input().strip()]}

score = {participant: [prod(participants[participant]), sum(participants[participant])] for participant in participants.keys()}.items()

score = sorted(score, key = lambda x: (x[1][0],x[1][1],x[0]))

print(' '.join(list(str(p[0]) for p in score[:3])))