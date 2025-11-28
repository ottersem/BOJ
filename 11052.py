import sys
input = sys.stdin.readline

def solution(n):
    cards = [0] + list(map(int,input().split()))
    dp = [0 for _ in range(n+1)]
    for i in range(n+1):
        for j in range(1, i+1):
            dp[i] = max(dp[i], cards[j] + dp[i-j])
    print(dp[n])
    print(dp)
    return

solution(int(input()))