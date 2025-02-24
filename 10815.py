n = int(input())
myCards = set(x for x in map(int, input().split()))
m = int(input())
yourCards = {x: '0' for x in map(int, input().split())}
for card in yourCards.keys():
    if card in myCards:
        yourCards[card] = '1'
print(' '.join(yourCards.values()))
