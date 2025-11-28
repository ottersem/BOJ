n = int(input())
m = 10007
DP = [[1] * 10]
for i in range(1,n+1):
    print('i : ', i)
    tmp = [0] * 10
    for j in range(10):
        tmp[j] = sum(DP[-1][j:]) % m
    print('tmp : ', tmp)
    DP.append(tmp)

print(DP[-1][0])
    
