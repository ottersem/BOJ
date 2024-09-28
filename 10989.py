from sys import stdin as sti
from itertools import accumulate

n = int(sti.readline())
arr = []
counting = list([0]*10000)

for _ in range(n):
    x = int(sti.readline())
    counting[x-1] += 1
    arr.append(x)

result = list([0]*len(arr))
counting = list(accumulate(counting))
arr.reverse()

for i in range(n):
    counting[arr[i]-1] -= 1
    result[counting[arr[i]-1]] += int(arr[i])

for j in range(n):
    print(result[j])
