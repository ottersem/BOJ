from sys import stdin as sti
n = int(sti.readline())
ls = []
for i in range(n):
    a = list(map(int, sti.readline().split()))
    ls.append(a)
ls.sort(key=lambda x: (x[1], x[0]))
for item in ls:
    print(item[0], item[1])