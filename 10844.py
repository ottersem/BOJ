def solution(n):
    DP = [[0] + [1] * 9]
    for _ in range(n-1):
        new_dp = []
        for i in range(10):
            if i == 0:
                new_dp.append(DP[-1][1])
                continue
            elif i == 9:
                new_dp.append(DP[-1][8])
                continue
            else:
                new_dp.append(DP[-1][i-1]+DP[-1][i+1])
        DP.append(new_dp)

    print(sum(DP[-1])%1000000000)
    
    

solution(int(input()))