from sys import stdin as sti


while True:
    line = list(sti.readline())
    if line[0] == '.' :
        break

    stack = []
    balanced = True
    for char in line:
        if char in'([':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balanced = False
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balanced = False
                break

    if balanced and not stack:
        print("yes")
    else:
        print("no")

