from sys import stdin as sti

n = int(sti.readline())

ls = []
nums = []
stack = []
ascend = True

for _ in range(n):
    ls.append(int(sti.readline()))

for i in range(n-1):
    if ls[i] == ls[0]:
        for _ in range(ls[i]):
            stack.append('+')
        stack.append('-')
    elif ls[i] < ls[i-1]:
        if ascend == True:
            for _ in range(ls[i-1]-ls[i]):
                stack.append('-')
            print('action 1')
        else:
            pass
    elif ls[i] > ls[i-1]:
        for _ in range(ls[i]-max(nums)):
            stack.append('+')
        stack.append('-')
        print('action 2')
        if ls[i] == n:
            ascend = False
    nums.append(ls[i])
    print(i, ls[i], stack)

if stack.count('+') == stack.count('-'):
    for j in stack:
        print(j)
else:
    print('NO')
