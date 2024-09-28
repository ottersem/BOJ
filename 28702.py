from sys import stdin as sti
ls = []
n = ''
for _ in range(3):
    ls.append(str(sti.readline()).strip())

def check(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
    
def FB(n):
    if n % 15 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n

if check(ls[2]):
    print(FB(int(ls[2])+1))
elif check(ls[1]):
    print(FB(int(ls[1])+2))
elif check(ls[0]):
    print(FB(int(ls[0])+3))