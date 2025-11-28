m = 15746
DP = [0,1]
for _ in range(int(input())-1):
    DP[0], DP[1] = DP[1], sum(DP)%m

print(sum(DP)%m)