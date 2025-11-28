DP = [(1,0)]
for _ in range(int(input())-1):
    DP.append((DP[-1][1], DP[-1][0]+DP[-1][1]))

print(sum(DP[-1]))