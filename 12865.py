import sys
input = sys.stdin.readline

def solution(n, k):
    items =[[0,0]] + [list(map(int, input().split())) for _ in range(n)]
    DP = [[0] *(k+1) for _ in range(n+1)]
    for i in range(n+1):
        weight, value = items[i]
        for w in range(k+1):
            if weight <= w:
                DP[i][w] = max(DP[i-1][w], DP[i-1][w-weight] + value)

            else:
                DP[i][w] = DP[i-1][w]
    
    print(DP[n][k])

n,k = map(int,input().split())
solution(n,k)