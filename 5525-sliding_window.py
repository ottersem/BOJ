from sys import stdin as sti

n = int(sti.readline())
m = int(sti.readline())
s = sti.readline().strip()

window, cnt, result = 0, 0, 0

while window < (m - 1):
    if s[window:window + 3] == 'IOI':
        count += 1
        window += 2
        if count == n:
            result += 1
            count -= 1
    else:
        window += 1
        count = 0

print(result)
