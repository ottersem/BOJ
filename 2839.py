n = int(input())

cnt = 0

if n % 5 == 0:
    print(n//5)
elif n == 4 or n == 7:
    print(-1)
else:
    while n % 5 != 0:
        if n >= 3:
            n -=3
            cnt += 1
        else:
            cnt = -1
    if cnt == -1:
        print(-1)
    else:
        while n != 0:
            n -= 5
            cnt += 1
    print(cnt)
    