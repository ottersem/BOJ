
T = int(input())
floor = [[0] * n for _ in range(k+1)]

for i in range(n): ##0층 채워넣기
    floor[0][i] = i+1

for ii in range(T):
    k = int(input())
    n = int(input())
    if floor[k][n-1] != 0:
        print(floor[k][n-1])
    else:
        for j in range(k+1):
            for r in range(n):
                floor[j][r] = sum(floor[j-1][:r+1])
                print(floor[j][r])

