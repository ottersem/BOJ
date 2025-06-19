n = list(map(int, input().strip()))
print(n)

length = len(n)

if length == 1:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
    exit()

first = n[0] - n[1]

for i in range(1,length-1):
    if n[i] - n[i+1] == first:
        continue
    else:
        print('흥칫뿡!! <(￣ ﹌ ￣)>')
        exit()

print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
