import sys
input = sys.stdin.readline

def solution(n):
    top =[0] + list(map(int, input().split()))
    bottom = [0] + list(map(int, input().split()))

    dp = [[0]*(n+1) for _ in range(3)]

    if n >= 1:
        dp[1][1] = top[1]
        dp[2][1] = bottom[1]

    for i in range(2, n+1):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + top[i]
        dp[2][i] = max(dp[0][i-1], dp[1][i-1]) + bottom[i]

    print(max(dp[0][n], dp[1][n], dp[2][n]))

for _ in range(int(input())):
    solution(int(input()))