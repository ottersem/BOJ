import sys
input = sys.stdin.readline

TTT = [[0]*3]*3
def checking(TTT):
    for hor in TTT: # horizontal
        if hor[0] == hor[1] and hor[1] == hor[2]:
            return hor[0]
    for i in range(3): # vertical
        if TTT[i][0] == TTT[i][1] and TTT[i][1] == TTT[i][2]:
            return TTT[i][0]
    # X
    if TTT[0][0] == TTT[1][1] and TTT[1][1] == TTT[2][2]:
        return TTT[1][1]
    if TTT[0][2] == TTT [1][1] and TTT[1][1] == TTT[2][0]:
        return TTT[1][1]
    return 0

n = int(input())
for i in range(9):
    a, b = map(int, input().split())
    TTT[a-1][b-1] = n
    c = checking(TTT)
    if  c != 0:
        print(c)
        break
    if n == 2:
        n = 1
    elif n == 1:
        n = 2
    if i == 8:
        print(0)