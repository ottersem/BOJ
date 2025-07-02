n,m = map(int,input().split())

if n == 1 and m == 1:
    print(0)

if min(n,m) == 1 and max(n,m) != 1:
    print(max(n,m)-1)

if min(n,m) != 1:
    print(n*m-1)