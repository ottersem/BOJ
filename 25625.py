x, y = map(int, input().split())

if x == y:
    print(0)
elif x < y:
    while x < y:
        y -= x
    print(y)
else:
    print(x+y)