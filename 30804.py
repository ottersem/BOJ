n = int(input())
s = list(map(int, input().split()))

count = [0] * 10 
left = 0
kind = 0
max_len = 0

for right in range(n):
    if count[s[right]] == 0:
        kind += 1
    count[s[right]] += 1
    
    while kind > 2:
        count[s[left]] -= 1
        if count[s[left]] == 0:
            kind -= 1
        left += 1
    
    max_len = max(max_len, right - left + 1)
    
print(max_len)
