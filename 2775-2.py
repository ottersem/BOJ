T = int(input())

for _ in range(T):#반복횟수
    k = int(input())
    n = int(input())
    try:
        floor[k][n-1]
    except NameError:
        floor = [[0] * n for _ in range(k+1)]
    except IndexError:
        floor = [[0] * n for _ in range(k+1)]

    for i in range(n):#조건 안에서 0층 채워넣기
        if floor[0][i] == 0:
            floor[0][i] = i+1

    if floor[k][n-1] != 0:
        pass
    else:
        for j in range(1,k+1):
            for r in range(n):
                floor[j][r] = sum(floor[j-1][:r+1])


    print(floor[k][n-1])