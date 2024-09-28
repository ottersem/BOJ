import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heard = set()
heardnseen = []

for _ in range(n):
    heard.add(input().strip())

for _ in range(m):
    name = input().strip()
    if name in heard:
        heardnseen.append(name)

heardnseen.sort()
print(len(heardnseen))
for name in heardnseen:
    print(name)