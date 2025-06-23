# Weekly
# Gredy

from sys import stdin
input = stdin.readline

def flip(pancake):
    if pancake == '+':
        return '-'
    elif pancake == '-':
        return '+'

for i in range(int(input())):
    s, k = input().split(); k=int(k); s = list(s.strip())
    cnt = 0
    for idx, pancake in enumerate(s):
        if pancake == '-':
            cnt += 1
            for j in range(k):
                s[idx+j] = flip(s[idx+j])
        
        if idx == len(s)-k:
            if '-' in s:
                print(f'Case #{i+1}: IMPOSSIBLE')
            else:
                print(f'Case #{i+1}: {cnt}') 
            break
