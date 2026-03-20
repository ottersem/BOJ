line = str(input())

answer = [] 

is_u = False
is_f = False

for char in line:
    if char == 'U':
        answer.append('U')
        is_u = True
        continue
    if char == 'F':
        if is_u == True:
            is_f = True
            answer.append('F')
        else:
            answer.append('-')
        continue
    
    if is_u and not is_f:
        answer.append('C')
    elif is_u and is_f:
        answer.append('-')
    else:
        answer.append('-')

print(''.join(answer))