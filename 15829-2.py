from sys import stdin as sti

L = int(sti.readline())
W = list(sti.readline().strip())
Result = 0

for i in range(L):
    Result += (ord(W[i]) - 96) * (31**i)
print(Result%1234567891)
