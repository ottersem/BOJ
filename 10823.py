import sys

nums = sys.stdin.read().strip()

nums_str = nums.replace('\n','')
num = list(map(int, nums_str.split(',')))

print(sum(num))

num = list(map(int, sys.stdin.read().strip().replace('\n','').split(',')))
print(sum(num))