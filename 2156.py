import sys
input = sys.stdin.readline

def solution(n):
    wine = [0] * n
    for i in range(n):
        wine[i] = int(input())

    if n == 1:
        print(wine[0])
        return
    if n == 2:
        print(wine[0] + wine[1])
        return

    dp = [[0] * 3 for _ in range(n)]

    dp[0][0] = 0
    dp[0][1] = wine[0]
    dp[0][2] = 0

    dp[1][0] = max(dp[0])
    dp[1][1] = wine[1]
    dp[1][2] = wine[0] + wine[1]   

    for i in range(2, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        dp[i][1] = dp[i-1][0] + wine[i]
        dp[i][2] = dp[i-1][1] + wine[i]

    print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))

solution(int(input()))