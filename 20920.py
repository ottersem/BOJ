from sys import stdin
from collections import Counter as cnter
import time
input = stdin.readline

n, m = map(int,input().split())
wordmaster = dict()

### 정석 ###
start1 = time.time()
for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue

    if not word in wordmaster:
        wordmaster[word] = 1
    else:
        wordmaster[word] += 1

answer = sorted(wordmaster.keys(), key = lambda x: (-wordmaster[x], -len(x), x))
end1  = time.time()

### counter 이용 ###
start2 = time.time()
words = [input().rstrip() for _ in range(n)]
filtering = [i for i in words if len(i) >= m]
counted = cnter(filtering)

answer = sorted(counted.keys(), key = lambda x: (-counted[x], -len(x), x))
end2 = time.time()

for word in answer:
    print(word)

print(f'First try : {end1 - start1}, Second try : {end2 - start2}')
