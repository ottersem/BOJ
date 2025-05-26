import math
n, k = map(int, input().split())

sum = math.factorial(n)//(math.factorial(k)*math.factorial(n-k))

print(int(sum%10007))