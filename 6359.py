import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = [False] * (n+1)

    for i in range(1,n+1):
        for j in range(i,n+1,i):
            nums[j] = not nums[j]

    cnt = sum(nums[1:])
    print(cnt)