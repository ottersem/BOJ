import sys
input = sys.stdin.readline

n, m, crt = map(int, input().split())

end_mo = m // 2 + 1

while True:
    tofu = int(input())
    
    if tofu == end_mo:
        print(0)
        break
    
    if tofu > end_mo:
        steps = tofu - end_mo
        next_host = ((crt - 1 + steps) % n) + 1
    else:
        steps = end_mo - tofu
        next_host = ((crt - 1 - steps) % n) + 1
    
    print(next_host)
    crt = next_host