from sys import stdin
input = stdin.readline

n, game = input().split()
p = set()

for _ in range(int(n)):
    user = str(input().strip())
    p.add(user)

if game == 'Y':
    print(len(p))
elif game == 'F':
    print(len(p)//2)
else:
    print(len(p)//3)
