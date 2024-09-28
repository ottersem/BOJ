from sys import stdin as sti

n = int(sti.readline())

ls = []
nums = []
stack = []
ascend = True

for _ in range(n):
    ls.append(int(sti.readline()))

for i in range(n):
    if ascend:
        if i == 0 or ls[i] > ls[i-1]:
            for _ in range(ls[i] - (ls[i-1] if i > 0 else 0)):
                stack.append('+')
            stack.append('-')
            if ls[i] == n:
                ascend = False
        elif ls[i] < ls[i-1]:
            for _ in range(ls[i-1] - ls[i]):
                stack.append('-')
        nums.append(ls[i])
    else:
        if ls[i] < ls[i-1]:
            stack.append('-')
        else:
            print("NO")
            exit()

for j in stack:
    print(j)