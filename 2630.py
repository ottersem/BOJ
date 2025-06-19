from sys import stdin
from collections import Counter
input = stdin.readline

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

def cutting(paper):
    cutted1 = paper[0:n//2+1][0:n//2+1]
    cutted2 = paper[0:n//2+1][n//2+1:n+1]
    cutted3 = paper[n//2+1:n+1][0:n//2+1]
    cutted4 = paper[n//2+1:n+1][n//2+1:n+1]

    return cutted1, cutted2, cutted3, cutted4

idle = [paper]

while idle:
    curr = idle.pop()
    a,b,c,d = cutting(paper, n=n)
    idle.append(a,b,c,d)
    n //=2

print(Counter.)