import sys
from itertools import groupby
input = sys.stdin.readline

code, string = map(str, input().split())

if code == 'E':
    answer = ''.join(f"{char}{len(list(group))}" for char, group in groupby(string))
    print(answer)
else:
    print("".join([string[char] * int(string[char + 1]) for char in range(0, len(string), 2)]))
