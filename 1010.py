import sys
import math
input = sys.stdin.readline

def solution(n):
    for _ in range(n):
        a, b = map(int, input().split())
        print(math.comb(b,a))

    return

solution(int(input()))