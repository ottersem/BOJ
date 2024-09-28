n = int(input())
a=1
count = 0

for i in range(n):
    a *= n-i

while a % 10 == 0:
    a //= 10
    count += 1

print(count)
n = int(input())
print(n//5+n//25+n//125)