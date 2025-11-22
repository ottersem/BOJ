import sys
input = sys.stdin.readline

def sol(n):
    cost = [list(map(int, input().split())) for _ in range(n)]
    DP = [cost[0]]

    for i, house in enumerate(cost):
        if i == 0 : continue

        tmp = []

        for j, color in enumerate(house):
            if j == 0:
                tmp.append(min(color + DP[i-1][1], color + DP[i-1][2]))
            elif j == 1:
                tmp.append(min(color + DP[i-1][0], color + DP[i-1][2]))
            elif j == 2:
                tmp.append(min(color + DP[i-1][1], color + DP[i-1][0]))
        DP.append(tmp)

    print(min(DP[-1]))

sol(int(input()))