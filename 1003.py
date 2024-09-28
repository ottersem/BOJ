import sys
input = sys.stdin.readline

n = int(input())

fibo = [[1, 0], [0, 1]]

for _ in range(n):
    t = int(input())
    while len(fibo) <= t:
        fibo.append([fibo[-2][0] + fibo[-1][0], fibo[-2][1] + fibo[-1][1]])
    print(fibo[t][0], fibo[t][1])