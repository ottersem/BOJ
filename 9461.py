import sys
input = sys.stdin.readline

memo = {}
val = [1,1,1,2,2,3,4,5,7,9]
for i in range(1,11):
    memo[i] = val[i-1]

for _ in range(int(input())):
    n = int(input())
    if n in memo:
        print(memo[n])
        continue
    else :
        for i in range(10,n+1):
            if n in memo:
                continue
            else:
                memo[i] = memo[i-3] + memo[i-4] + memo[i-5]
        print(memo[n])

        
