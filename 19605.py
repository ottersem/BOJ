t = str(input())
s = str(input())
s_list = []

for _ in range(len(s)):
    s_list.append(s)
    s = s[1:] + s[0] 

print(s_list)

for componenet in s_list:
    if componenet in t:
        print('yes')
        exit(0)

print('no')