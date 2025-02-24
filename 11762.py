import sys
from itertools import combinations
input = sys.stdin.readline

ipt = list(map(int, input().split()))
boxes, heights = ipt[:6], ipt[-2:]
answer = []

for height in heights:
    for comb in combinations(boxes, 3):
        if sum(comb) == height:
            comb = sorted(comb, reverse= True)
            answer.extend(comb)

print(' '.join(map(str, answer)))