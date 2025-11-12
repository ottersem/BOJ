from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix[i][j] | (matrix[i][k] & matrix[k][j])

for row in matrix:
    row = map(str, row)
    print(' '.join(row))