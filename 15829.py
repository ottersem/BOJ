from sys import stdin as sti

L = int(sti.readline())
W = list(sti.readline().strip())
Result = 0
num = 1234567891

def str2int(n):
    return ord(n) - ord('a') + 1

for i in range(L):
    Result += str2int(W[i])*(31**i)
if Result < num:
    print(Result)
else:
    print(Result % num)
    