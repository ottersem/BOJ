import sys
input = sys.stdin.readline

n = int(input())
memo = {}
memo[1] = 1
memo[2] = 2
memo[3] = 3

for i in range(4, n+1):
    memo[i] = memo[i-1] + memo[i-2] 
    memo[i] = memo[i] %10007
    
print(memo[n])