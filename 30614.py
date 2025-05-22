from sys import stdin
input = stdin.readline

num = int(input())
actions = list(input().strip())

stack = []

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for action in actions:
    if action in lower:
        stack.append(action)
    elif action in upper:
        if stack and stack[-1] == action.lower():
            stack.pop()
        else:
            stack.append(action)

print(1 if not stack else 0)