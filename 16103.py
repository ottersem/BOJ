import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = n // 4
b = n // 2
string = input().strip()

def transform(s):
    return s[:a] + s[n-a:] + s[a:a+b] + s[a+b:n-a]

original = string
current = string

for i in range(1, min(k + 1, n + 1)):
    current = transform(current)
    if current == original:
        k = k % i
        break

result = string
for _ in range(k):
    result = transform(result)

print(result)