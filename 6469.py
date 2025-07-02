import sys
from math import gcd

for line in sys.stdin:
    if not line.strip():
        continue
    step, mod = map(int, line.split())

    result = "Good Choice" if gcd(step, mod) == 1 else "Bad Choice"
    print(f"{step:>10}{mod:>10} {result}\n")