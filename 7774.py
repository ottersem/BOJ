n, m = map(int,input().split())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

if n == 0 or m == 0:
    print(1)
    exit()

condition_a = a.pop()
condition_b = 0
max = 0

while len(a) != 0 or len(b) != 0:
    while condition_a != 0:
        if len(b) == 0:
            break
        condition_b += b.pop()
        condition_a -= 1
        if condition_b > max:
            max = condition_b

    while condition_b != 0:
        if len(a) == 0:
            break
        condition_a += a.pop()
        condition_b -= 1
    
print(max)
