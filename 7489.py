import math

for _ in range(int(input())):
    n = str(math.factorial(int(input())))
    
    for num in n[::-1]:
        if num == '0':
            continue
        else:
            print(num)
            break

