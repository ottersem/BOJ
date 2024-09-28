from sys import stdin as sti

n = int(sti.readline())

ls = []
nums = []
stack = []
ascend = True

for _ in range(n):
    ls.append(int(sti.readline()))

for i in range(n):
    if ascend == True:
        if ls[i] == ls[0]:
            for _ in range(ls[i]):
                stack.append('+')
            stack.append('-')
        elif ls[i] < ls[i-1]:
            for _ in range(ls[i-1]-ls[i]):
                stack.append('-')
        elif ls[i] > ls[i-1]:
            for _ in range(ls[i]-max(nums)):
                stack.append('+')
            stack.append('-')
            if ls[i] == n:
                ascend = False   
        nums.append(ls[i])        
    elif ascend == False:
        if ls[i] < ls[i-1]:
            stack.append('-')  
        else:
            exit("NO")
            
for j in stack:
    print(j)