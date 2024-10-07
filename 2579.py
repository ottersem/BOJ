import sys
input = sys.stdin.readline

n = int(input())
dp = {}

stairs = {0: 0}
for i in range(1, n+1):
    stairs[i] = int(input())

if n<3:
    print(sum(stairs.values()))
    exit()

dp[0] = 0
dp[1] = stairs[1]
dp[2] = stairs[1]+stairs[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-2], dp[i-3]+stairs[i-1]) + stairs[i]
print(dp[n])
