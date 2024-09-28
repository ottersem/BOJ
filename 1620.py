import sys
input = sys.stdin.readline
dic = []

n, m = map(int, input().split())
for _ in range(n):
    dic.append(input().strip())
for _ in range(m):
    k = input()
    try:
        int(k)
        print(dic[int(k)-1])
    except ValueError:
        print(dic.index(k.strip())+1)

