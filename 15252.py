import sys
input = sys.stdin.readline

for x in range(int(input())):
    print(f"Data Set {x+1}:")
    c, n = map(int, input().split())
    country = [int(x) for x in input().split()]
    for num in input().split():
        country[int(num)-1] -= 1
    print(max(country))
    print('')
