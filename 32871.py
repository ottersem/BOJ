from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n > m:
        n, m = m, n
    if n == 1:
        print("YES")
    elif (m - n) % 2 == 0:
        print("NO")
    else:
        print("YES")