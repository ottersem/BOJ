a, b = map(int, input().split())

if a < b+1 or a > b*2:
    print("NO")
    exit()
else:
    print("YES")

tmp = b + 1
k = 1

while tmp != a:
    tmp += 1
    k += 1

print(k)

the_1st_burger = 'ab'*(b-k+1)+'a'
print(the_1st_burger)
for _ in range(k-1):
    print('aba')