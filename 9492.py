import sys
input = sys.stdin.readline

while True:
    n = int(input())

    answer = list([0]*(n+1))

    if n == 0:
        break
    elif n % 2 == 0:
        for i in range(1,n+1):
            card = str(input().strip())
            if i <= n//2:
                answer[i*2-1] = card
            else:
                answer[i*2-n] = card
    else:
        for i in range(1, n+1):
            card = str(input().strip())
            if i <= n//2+1:
                answer[i*2-1] = card
            else:
                answer[i*2-(n+1)] = card
    for card in answer:
        if card == 0:
            continue
        print(card)