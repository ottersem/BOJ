from sys import stdin
import time
input = stdin.readline

c, h = map(int, input().split())

upper = []
lower = []

for i in range(c):
    train = str(input())
    