from sys import stdin
input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))

idx = sorted(list(set(nums[:])))
co = {v : i for i, v in enumerate(idx)}

comp = [co[x] for x in nums]
print(*comp)