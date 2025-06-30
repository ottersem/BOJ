n,b,h,w = map(int,input().split())

hotels = dict()

answer = 500001

for _ in range(h):
    p = int(input())
    a = list(map(int, input().split()))

    if max(a) < n:
        continue
    else:
        fee = p * n
        if fee <= b:
            if answer > fee:
                answer = fee

print('stay home' if answer == 500001 else answer)