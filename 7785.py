import sys
input = sys.stdin.readline

employee = {}
for _ in range(int(input())):
    name, status = map(str, input().split())
    if name in employee.keys():
        employee.pop(name)
    else:
        employee[name] = 1
print('\n'.join(sorted(employee.keys(), reverse=True)))