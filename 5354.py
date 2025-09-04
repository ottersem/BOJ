import sys
input = sys.stdin.readline

c = int(input())
for i in range(c):
    n = int(input())
    if n == 1:
        print('#')
        print()
        continue

    print('#'*n)

    for _ in range(n-2):
        print('#'+('J'*(n-2))+'#')

    print('#'*n)
    if i < c-1:
        print()

