num = list(input().strip())
index = num.index('*')

def isbn(arr):
    answer = []
    for i in arr[:-2]:
        if int(i) % 2 == 0:
            answer.append(i)
        else:
            answer.append(str(int(i)*3))
    n = int(''.join(answer))
    if n % int(arr[-1]) == 0:
        return True
    else:
        return False

for i in range(10):
    num[index] = str(i)
    if isbn(num):
        print(i)
        break



