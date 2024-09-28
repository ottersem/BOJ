import sys
input = sys.stdin.readline

M = int(input())

ls = [False]*21

for _ in range(M):
    cmd = input().split()
    if len(cmd) == 1:
        if cmd[0] == "all":
            ls = [True] * 21
        elif cmd[0] == "empty":
            ls = [False] * 21
    elif len(cmd) == 2:
        index = int(cmd[1])
        match cmd[0]:
            case "add":
                ls[index] = True
            case "remove":
                ls[index] = False
            case "check":
                print(1 if ls[index] else 0)
            case "toggle":
                ls[index] = not ls[index]

