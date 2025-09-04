problem = list(map(str, input().strip()[::-1]))

string = 'abcdefghijklmnopqrstuvwxyz'

cnt=0

while len(problem) > 0:
    for char in string:
        if problem:
            if problem[-1] == char:
                problem.pop()
    cnt += 1

print(cnt)
