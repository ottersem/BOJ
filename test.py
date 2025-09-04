import sys
input = sys.stdin.readline

orange = 'orange'
game = str(input().strip())
cnt = 0
i = 0

for j in range(len(game)):
    if game[j] == orange[i]:
        cnt += 1
        continue
    elif game[j] == orange[i+1]:
        cnt += 1
        i += 1
    else:
        cnt = 0
        i = 0

print(cnt)
    