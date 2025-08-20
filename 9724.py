import sys
import math
input = sys.stdin.readline

for i in range(int(input())):
    a, b = map(int, input().split())

    s = int(math.ceil(math.cbrt(a)))

    while s**3 < a:
        s += 1

    e = int(math.floor(math.cbrt(b)))

    while (e+1)**3 <= b:
        e += 1

    cnt = max(0, e-s+1)

    print(f'Case #{i+1}: {cnt}')